from Game import Piece, Position

P_gen = Position.Position

class Queen(Piece.Piece):
    def __init__(self, board, P_s=(0,0), color=True):
        Piece.Piece.__init__(self, board, P_s, 'Q', color)

    def valid_move(self, P_n):
        d_x = abs(P_n.x - self.P_c.x)
        dsp_x = P_n.x - self.P_c.x
        d_y = abs(P_n.y - self.P_c.y)
        dsp_y = P_n.y - self.P_c.y

        # Check if new position if out of board
        if self.board.out_of_board(P_n):
            return False

        # Check if there is a piece on P_n, and if it is a take
        R_P_n = self.board.get_piece(P_n)
        if R_P_n[0]:
            if R_P_n[1].color == self.color:
                return False

        # Diagonal movement
        if d_x != 0 and d_y != 0 and d_x == d_y:

            C_x_t = []
            if dsp_x > 0:
                C_x_t = list(xrange(self.P_c.x, P_n.x, 1))
            else:
                C_x_t = list(xrange(P_n.x, self.P_c.x, 1))

            # Generate Y-coordinates along Bishop move path
            C_y_t = []
            if dsp_y > 0:
                C_y_t = list(xrange(self.P_c.y, P_n.y, 1))
            else:
                C_y_t = list(xrange(P_n.y, self.P_c.y, 1))

            # Generate (X,Y) pairs along move path, not including start and end
            C_xy_t = []
            for x in C_x_t:
                for y in C_y_t:
                    C_xy_t.append([x, y])

            # Creates Position objects for each (X,Y) pair
            Ps_c = map(lambda C_xy: P_gen(C_xy[0], C_xy[1]), C_xy_t)

            # Checks if there are Pieces in path
            for P_c in Ps_c:
                if P_c.x not in [P_n.x, self.P_c.x] and \
                                P_c.y not in [P_n.y, self.P_c.y]:
                    R_P_c = self.board.get_piece(P_c)
                    if R_P_c[0]:
                        return False

            return True

        # Single-direction on Y
        elif d_x == 0 and d_y != 0:
            # Compute list of Y-coords to traverse
            if dsp_y < 0:
                C_y_t = list(xrange(P_n.y, self.P_c.y, 1))
            else:
                C_y_t = list(xrange(self.P_c.y, P_n.y, 1))
            # Create position objects to traverse
            Ps_c = map(lambda y: P_gen(P_n.x, y), C_y_t)
            # Check if path is clear
            for P_c in Ps_c:
                if P_c.y not in [P_n.y, self.P_c.y]:
                    R_P_c = self.board.get_piece(P_c)
                    if R_P_c[0]:
                        return False
            return True

        # Single direction on X
        elif d_y == 0 and d_x != 0:
            # Compute list of X-coords to traverse
            if dsp_x < 0:
                C_x_t = list(xrange(P_n.x, self.P_c.x, 1))
            else:
                C_x_t = list(xrange(self.P_c.x, P_n.x, 1))
            # Create position objects to traverse
            Ps_c = map(lambda x: P_gen(x, P_n.y), C_x_t)
            # Check if path is clear
            for P_c in Ps_c:
                if P_c.x not in [P_n.x, self.P_c.x]:
                    R_P_c = self.board.get_piece(P_c)
                    if R_P_c[0]:
                        return False
            return True

        # Other movement is invalid
        else:
            return False