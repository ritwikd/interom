from Game import Piece, Position

generate_position = Position.Position

class King(Piece.Piece):
    def __init__(self, board, position_start=(0,0), color=True):
        Piece.Piece.__init__(self, board, position_start, 'K', color)

    def valid_move(self, position_new):
        delta_x = abs(position_new.x - self.position_current.x)
        displacement_x = position_new.x - self.position_current.x
        delta_y = abs(position_new.y - self.position_current.y)
        displacement_y = position_new.y - self.position_current.y

        # Check if new position if out of board
        if self.board.out_of_board(position_new):
            return False

        # Check if there is a piece on position_new, and if it is a take
        position_new_store = self.board.get_piece(position_new)
        if position_new_store[0]:
            if position_new_store[1].color == self.color:
                return False

        # Y-axis movement greater than 1 is always invalid
        if delta_y > 1 or delta_x > 2:
            return False

        # X-axis movement greater than 1 is potentially castling
        if delta_x > 1:
            # Check for castle condition
            x_cond = self.position_current.x == 4
            rank_cond = (self.position_current.y == 0 and self.color) or \
                        (self.position_current.y == 7 and not self.color)
            castle_cond = x_cond and rank_cond
            if delta_y != 0 or not castle_cond:
                return False

            # Check if last move caused check on this king
            previous_move = self.board.log.get_last_move()
            if previous_move[0]:
                if previous_move[1].check and previous_move[1].color != self.color:
                    return False

            # Check if path is clear
            if displacement_x < 0:
                current_x_path = list(range(position_new.x, self.position_current.x, 1))
            else:
                current_x_path = list(range(self.position_current.x, position_new.x, 1))
            piece_conflict = [generate_position(x, position_new.y) for x in current_x_path]
            for position_current in piece_conflict:
                if position_current.x not in [self.position_current.x]:
                    position_check = self.board.get_piece(position_current)
                    if position_check[0] or self.board.potential_check_square(position_current, self.color):
                        return False

            # Find rook and check if it exists
            P_rook = generate_position(0, self.position_current.y)
            if displacement_x > 0:
                P_rook.x == 7
            R_rook = self.board.get_piece(P_rook)
            if not R_rook[0]:
                return False
            if R_rook[1].type != 'R':
                return False

            # Check if King or Rook has moved before
            move_history = self.board.log.get_move_history()
            for move in move_history:
                if move.Piece == self or move.Piece == R_rook[1]:
                    return False

            return True

        valid_non_castle_m_pats = [delta_x == 1 and delta_y == 1,
                                   delta_x == 1 and delta_y == 0,
                                   delta_x == 0 and delta_y == 1]

        return True in valid_non_castle_m_pats
