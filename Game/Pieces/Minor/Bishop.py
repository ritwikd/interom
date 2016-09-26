import Game

class Bishop(Game.Piece.Piece):
    def __init__(self, board, P_s=(0,0), color=True):
        Game.Piece.Piece.__init__(self, board, P_s, 'B', color)

    def valid_move(self, P_n):
        # TODO: Implement valid move checker for bishop
        pass
