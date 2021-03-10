from Game import Piece, Position

generate_position = Position.Position

class Bishop(Piece.Piece):
    def __init__(self, board, position_start=(0,0), color=True):
        Piece.Piece.__init__(self, board, position_start, 'B', color)

    def valid_move(self, position_new):
        delta_x = abs(position_new.x - self.position_current.x)
        delta_y = abs(position_new.y - self.position_current.y)
        displacement_x = position_new.x - self.position_current.x
        displacement_y = position_new.y - self.position_current.y

        if self.board.out_of_board(position_new):
            return False

        if delta_x != delta_y:
            return False

        # Check if take, or invalid (same color piece)
        position_new_store = self.board.get_piece(position_new)
        if position_new_store[0]:
            if position_new_store[1].color == self.color:
                return False

        # Generate X-coordinates along Bishop move path
        x_coordinate_store = []
        if displacement_x > 0:
            x_coordinate_store = list(range(self.position_current.x, position_new.x, 1))
        else:
            x_coordinate_store = list(range(position_new.x, self.position_current.x, 1))

        # Generate Y-coordinates along Bishop move path
        y_coordinate_store = []
        if displacement_y > 0:
            y_coordinate_store = list(range(self.position_current.y, position_new.y, 1))
        else:
            y_coordinate_store = list(range(position_new.y, self.position_current.y, 1))

        # Generate (X,Y) pairs along move path, not including start and end
        xy_tuple_store = []
        for x in x_coordinate_store:
            for y in y_coordinate_store:
                    xy_tuple_store.append([x,y])

        # Creates Position objects for each (X,Y) pair
        piece_conflict = [generate_position(xy_tuple[0], xy_tuple[1]) for xy_tuple in xy_tuple_store]

        # Checks if there are Pieces in path
        for position_current in piece_conflict:
            if position_current.x not in [position_new.x, self.position_current.x] and \
                            position_current.y not in [position_new.y, self.position_current.y]:
                position_check = self.board.get_piece(position_current)
                if position_check[0]:
                    return False

        return True
