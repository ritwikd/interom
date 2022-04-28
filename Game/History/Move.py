class Move:
    def __init__(self, color, Piece, position_original, position_new, take=False, Piece_t=None,
                 check=False, mate=False, castle=None):
        self.color = color
        self.Piece = Piece
        self.Position_original = position_original
        self.position_new = position_new

        self.take = take
        self.Piece_t = Piece_t

        self.check = check

        self.castle = castle

        self.mate = mate
