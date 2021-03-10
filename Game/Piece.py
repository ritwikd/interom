class Piece:
    def __init__(self, board, position_start=(0,0), type=None, color=True):
        self.position_current = position_start
        self.board = board
        self.type = type
        self.color = color

    def valid_move(self, position_new):
        target = self.board.get_piece(position_new)
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







