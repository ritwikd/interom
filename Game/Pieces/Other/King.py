from Game import Piece

class King(Piece.Piece):
    def __init__(self, board, P_s=(0,0), color=True):
        Piece.Piece.__init__(self, board, P_s, 'K', color)

    def valid_move(self, P_n):
        # TODO: Implement valid move checker for king
        # x_cond = P_o.x == 3
        # rank_cond = (P_o.y == 0 and white_move) or \
        #             (P_o.y == 7 and not white_move)
        # move_cond = abs(P_n.x - P_o.x) == 2 and P_n.y - P_o.y == 0
        pass
