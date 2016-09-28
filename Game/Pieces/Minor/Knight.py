from Game import Piece

class Knight(Piece.Piece):
    def __init__(self, board, P_s=(0,0), color=True):
        Piece.Piece.__init__(self, board, P_s, 'N', color)

    def valid_move(self, P_n):
        d_x = abs(P_n.x - self.P_c.x)
        d_y = abs(P_n.y - self.P_c.y)

        if self.board.out_of_board(P_n):
            return False

        # Check if knight P_n contains same-color piece
        R_P_n =  self.board.get_piece(P_n)
        if R_P_n[0]:
            if R_P_n[1].color == self.color:
                return False

        # Check if movement is valid for Knight (2x1 L-shape)
        if (d_x == 2 and d_y == 1 or d_y == 1 and d_x == 2):
            return True
        else:
            return False
