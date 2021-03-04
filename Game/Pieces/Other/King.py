from Game import Piece, Position

P = Position.Position

class King(Piece.Piece):
    def __init__(self, board, P_s=(0,0), color=True):
        Piece.Piece.__init__(self, board, P_s, 'K', color)

    def valid_move(self, P_n):
        d_x = abs(P_n.x - self.P_c.x)
        dsp_x = P_n.x - self.P_c.x
        d_y = abs(P_n.y - self.P_c.y)
        dsp_y = P_n.y - self.P_c.y

        # Check if new position if out of board
        if self.board.out_of_board(P_n):
            return False

        # Check if there is a piece on P_n, and if it is a take
        R_P_n = self.board.get_piece(P_n)
        if R_P_n[0]:
            if R_P_n[1].color == self.color:
                return False

        # Y-axis movement greater than 1 is always invalid
        if d_y > 1 or d_x > 2:
            return False

        # X-axis movement greater than 1 is potentially castling
        if d_x > 1:
            # Check for castle condition
            x_cond = self.P_c.x == 4
            rank_cond = (self.P_c.y == 0 and self.color) or \
                        (self.P_c.y == 7 and not self.color)
            castle_cond = x_cond and rank_cond
            if d_y != 0 or not castle_cond:
                return False

            # Check if last move caused check on this king
            M_l = self.board.log.get_last_move()
            if M_l[0]:
                if M_l[1].check and M_l[1].color != self.color:
                    return False

            # Check if path is clear
            if dsp_x < 0:
                C_x_t = list(range(P_n.x, self.P_c.x, 1))
            else:
                C_x_t = list(range(self.P_c.x, P_n.x, 1))
            Ps_c = [P(x, P_n.y) for x in C_x_t]
            for P_c in Ps_c:
                if P_c.x not in [self.P_c.x]:
                    R_P_c = self.board.get_piece(P_c)
                    if R_P_c[0] or self.board.potential_check_square(P_c, self.color):
                        return False

            # Find rook and check if it exists
            P_rook = P(0, self.P_c.y)
            if dsp_x > 0:
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

        valid_non_castle_m_pats = [d_x == 1 and d_y == 1,
                                   d_x == 1 and d_y == 0,
                                   d_x == 0 and d_y == 1]

        return True in valid_non_castle_m_pats
