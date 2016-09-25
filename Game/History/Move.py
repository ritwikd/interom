import Game.Board as Board


class Move:
    def __init__(self, color, Piece, P_o, P_n, take=False, Piece_t=None,
                 check=False, mate=False, castle=None):
        self.color = color
        self.Piece = Piece,
        self.P_o = P_o
        self.P_n = P_n

        self.take = take
        self.Piece_t = Piece_t

        self.check = check

        self.castle = castle

        self.mate = mate
