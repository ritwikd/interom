from Game import Piece

class Knight(Piece.Piece):
    def __init__(self, board, P_s=(0,0), color=True):
        Piece.Piece.__init__(self, board, P_s, 'N', color)

    def valid_move(self, P_n):
        d_x = abs(P_n.x - self.P_c.x)
        d_y = abs(P_n.y - self.P_c.y)

        # Get board info for new position (P_n)
        R_P_n =  self.board.get_piece(P_n)
        if R_P_n[0]:
            # Check if same-color piece there
            if R_P_n[1].color != self.color:
                # Check if valid knight pattern
                if (d_x == 2 and d_y == 1 or d_y == 1 and d_x == 2):
                    return True
                else:
                    return False
            else:
                return False
        else:
            # Check if valid knight pattern
            if (d_x == 2 and d_y == 1 or d_y == 1 and d_x == 2):
                return True
            else:
                return False
