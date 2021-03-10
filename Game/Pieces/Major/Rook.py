from Game import Piece, Position

generate_position = Position.Position

class Rook(Piece.Piece):
    def __init__(self, board, position_start=(0,0), color=True):
        Piece.Piece.__init__(self, board, position_start, 'R', color)

    def valid_move(self, position_new):
        # Compute deltas and displacement for new move
        delta_x = abs(position_new.x - self.position_current.x)
        displacement_x = position_new.x - self.position_current.x
        delta_y = abs(position_new.y - self.position_current.y)
        displacement_y = position_new.y - self.position_current.y
        # Check if position is out of board
        if self.board.out_of_board(position_new):
            return False
        # Validate single-direction movement
        if delta_x != 0 and delta_y != 0:
            return False
        # Check if there is a piece on position_new, and if it is a take
        position_new_store = self.board.get_piece(position_new)
        if position_new_store[0]:
            if position_new_store[1].color == self.color:
                return False

        # Movement on X-axis
        if delta_x != 0 and delta_y == 0:
            # Compute list of X-coords to traverse
            if displacement_x < 0:
                x_coordinate_store = list(range(position_new.x, self.position_current.x, 1))
            else:
                x_coordinate_store = list(range(self.position_current.x, position_new.x, 1))
            # Create position objects to traverse
            piece_conflict = [generate_position(x, position_new.y) for x in x_coordinate_store]
            # Check if path is clear
            for position_current in piece_conflict:
                if position_current.x not in [position_new.x, self.position_current.x]:
                    position_check = self.board.get_piece(position_current)
                    if position_check[0]:
                        return False
            return True

        # Movement on Y-axis
        elif delta_x == 0 and delta_y != 0:
            # Compute list of Y-coords to traverse
            if displacement_y < 0:
                y_coordinate_store = list(range(position_new.y, self.position_current.y, 1))
            else:
                y_coordinate_store = list(range(self.position_current.y, position_new.y, 1))
            # Create position objects to traverse
            piece_conflict = [generate_position(position_new.x, y) for y in y_coordinate_store]
            # Check if path is clear
            for position_current in piece_conflict:
                if position_current.y not in [position_new.y, self.position_current.y]:
                    position_check = self.board.get_piece(position_current)
                    if position_check[0]:
                        return False
            return True




