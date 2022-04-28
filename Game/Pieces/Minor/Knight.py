from Game import Piece

class Knight(Piece.Piece):
    def __init__(self, board, position_start=(0,0), color=True):
        Piece.Piece.__init__(self, board, position_start, 'N', color)

    def valid_move(self, position_new):
        delta_x = abs(position_new.x - self.P_c.x)
        delta_y = abs(position_new.y - self.P_c.y)

        if self.board.out_of_board(position_new):
            return False

        # Check if knight position_new contains same-color piece
        position_new_store =  self.board.get_piece(position_new)
        if position_new_store[0]:
            if position_new_store[1].color == self.color:
                return False

        # Check if movement is valid for Knight (2x1 L-shape)
        if (delta_x == 2 and delta_y == 1 or delta_y == 1 and delta_x == 2):
            return True
        else:
            return False
