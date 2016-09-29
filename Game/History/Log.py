class Log:
    def __init__(self):
        self.moves = []

    def add_move(self, move):
        self.moves.append(move)

    def get_move(self, index):
        if index < len(self.moves):
            return [True, self.moves[index]]
        else:
            return -1

    def get_last_move(self):
        if len(self.moves) == 0:
            return [False]
        else:
            return [True, self.moves[-1]]

    def get_move_history(self):
        return self.moves