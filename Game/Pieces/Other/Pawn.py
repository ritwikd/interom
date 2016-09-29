from Game import Piece, Position

P = Position.Position

class Pawn(Piece.Piece):
    def __init__(self, board, P_s=(0,0), color=True):
        Piece.Piece.__init__(self, board, P_s, 'P', color)

    def valid_move(self, P_n):
        d_x = abs(P_n.x - self.P_c.x)
        dsp_x = P_n.x - self.P_c.x
        d_y = abs(P_n.y - self.P_c.y)
        dsp_y = P_n.y - self.P_c.y

        # Check if new position if out of board
        if self.board.out_of_board(P_n):
            return False

        # Make sure P_n is empty or take-able
        R_P_n = self.board.get_piece(P_n)
        if R_P_n[0]:
            if R_P_n[1].color == self.color:
                return False
            else:
                if d_x == 0:
                    return False
                else:
                    if d_y > 1:
                        return False

        # Check if direction is correct
        if (dsp_y > 0) != self.color:
            return False

        # Potential first-move 2-space move
        if d_y == 2:
            # No takes or lateral movement
            if d_x != 0:
                return False

            # Must be on 2nd or 7th rank
            if (self.color and self.P_c.y != 1) or \
                (not self.color and self.P_c.y != 6):
                return False

            return True

        # Other moves
        if d_y == 1:

            if d_x > 1:
                return False

            # Diagonal move
            if d_x == 1:
                # Potential en-passant
                if not R_P_n[0]:
                    # Check if piece is in en-passant position
                    P_ep_p = P(P_n.x, self.P_c.y)
                    R_P_ep_p = self.board.get_piece(P_ep_p)
                    if not R_P_ep_p[0]:
                        return False
                    # Make sure piece in en-passant position is a pawn
                    ep_p = R_P_ep_p[1]
                    if ep_p.type != 'P':
                        return False
                    # Make sure pawn in en-passant position moved validly
                    M_last = self.board.log.get_last_move()
                    if not M_last[0]:
                        return False
                    M_last = M_last[1]
                    # Make sure piece moved last turn was en-passant pawn
                    if M_last.Piece != ep_p or M_last.Piece.color == self.color:
                        return False
                    # Make sure piece moved last turn moved 2 spaces
                    if abs(M_last.P_n.y - M_last.P_o.y) != 2:
                        return False

                    return True

                return True

            return True


        return False















