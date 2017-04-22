class Piece:
    def __init__(self, board, P_s=(0,0), type=None, color=True):
        self.P_c = P_s
        self.board = board
        self.type = type
        self.color = color

    def valid_move(self, P_n):
        target = self.board.get_piece(P_n)
        if target[0]:
            if target.color == self.color:
                return False
            else:
                # Handle movement constraints
                pass
                # Handle takes
                pass
        else:
            # Handle movement constraints
            pass







