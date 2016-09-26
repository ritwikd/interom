from Game import Piece

class Pawn(Piece.Piece):
    def __init__(self, board, P_s=(0,0), color=True):
        Piece.Piece.__init__(self, board, P_s, 'P', color)

    def valid_move(self, P_n):
        # TODO: Implement valid move checker for pawn
        pass
