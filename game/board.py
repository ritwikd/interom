class Board:
    def __init__(self):
        self.data = [[] * 8] * 8

        # Use for xy_to_alg conversion
        self.letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        self.numbers = map(lambda n: n + 1, range(8))

    def xy_to_alg(self, P_x, P_y):
        try:
            return self.letters[P_x] + self.numbers[P_y]
        except:
            return 'Invalid position.'





