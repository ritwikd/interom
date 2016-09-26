from Game import Piece, Position

P_gen = Position.Position

class Bishop(Piece.Piece):
    def __init__(self, board, P_s=(0,0), color=True):
        Piece.Piece.__init__(self, board, P_s, 'B', color)

    def valid_move(self, P_n):
        d_x = abs(P_n.x - self.P_c.x)
        d_y = abs(P_n.y - self.P_c.y)

        dsp_x = P_n.x - self.P_c.x
        dsp_y = P_n.y - self.P_c.y

        R_P_n = self.board.get_piece(P_n)

        if d_x == d_y:
            Ps_c = []

            # Generate X-coordinates along Bishop move path
            C_x_t = []
            if dsp_x > 0:
                C_x_t = xrange(self.P_c.x, P_n.x, 1)
            else:
                C_x_t = xrange(P_n.x, self.P_c.x, 1)

            # Generate Y-coordinates along Bishop move path
            C_y_t = []
            if dsp_y > 0:
                C_y_t = xrange(self.P_c.y, P_n.y, 1)
            else:
                C_y_t = xrange(P_n.y, self.P_c.y, 1)

            # Generate (X,Y) pairs along move path
            C_xy_t = []
            for x in C_x_t[1:]:
                for y in C_y_t[1:]:
                    C_xy_t  = [x,y]

            # Creates Position objects for each (X,Y) pair
            Ps_c = map(lambda C_xy: P_gen(C_xy[0], C_xy[1]), C_xy_t)

            # Checks if there are pieces in path
            E_path = True in map(lambda Ps_c: self.board.get_piece(Ps_c)[0], Ps_c)

        else:
            False
