from Game import Piece, Position

generate_position = Position.Position

class Pawn(Piece.Piece):
    def __init__(self, board, position_start=(0,0), color=True):
        Piece.Piece.__init__(self, board, position_start, 'P', color)

    def valid_move(self, position_new):
        delta_x = abs(position_new.x - self.position_current.x)
        displacement_x = position_new.x - self.position_current.x
        delta_y = abs(position_new.y - self.position_current.y)
        displacement_y = position_new.y - self.position_current.y

        # Check if new position if out of board
        if self.board.out_of_board(position_new):
            return False

        # Make sure position_new is empty or take-able
        position_new_store = self.board.get_piece(position_new)
        if position_new_store[0]:
            if position_new_store[1].color == self.color:
                return False
            else:
                if delta_x == 0:
                    return False
                else:
                    if delta_y > 1:
                        return False

        # Check if direction is correct
        if (displacement_y > 0) != self.color:
            return False

        # Potential first-move 2-space move
        if delta_y == 2:
            # No takes or lateral movement
            if delta_x != 0:
                return False

            # Must be on 2nd or 7th rank
            if (self.color and self.position_current.y != 1) or \
                (not self.color and self.position_current.y != 6):
                return False

            return True

        # Other moves
        if delta_y == 1:

            if delta_x > 1:
                return False

            # Diagonal move
            if delta_x == 1:
                # Potential en-passant
                if not position_new_store[0]:
                    # Check if piece is in en-passant position
                    piece_en_passant_position = generate_position(position_new.x, self.position_current.y)
                    en_passant_position_store = self.board.get_piece(piece_en_passant_position)
                    if not en_passant_position_store[0]:
                        return False
                    # Make sure piece in en-passant position is a pawn
                    en_passant_pawn = en_passant_position_store[1]
                    if en_passant_pawn.type != 'P':
                        return False
                    # Make sure pawn in en-passant position moved validly
                    previous_move = self.board.log.get_last_move()
                    if not previous_move[0]:
                        return False
                    previous_move = previous_move[1]
                    # Make sure piece moved last turn was en-passant pawn
                    if previous_move.Piece != en_passant_pawn or previous_move.Piece.color == self.color:
                        return False
                    # Make sure piece moved last turn moved 2 spaces
                    if abs(previous_move.position_new.y - previous_move.position_original.y) != 2:
                        return False

                    return True

                return True

            return True


        return False















