class Log:
    def __init__(self):
        self.moves = []

    def addMove(self, move):
        self.moves.append(move)

    def getMove(self, index):
        if index < len(self.moves):
            return [True, self.moves[index]]
        else:
            return -1

    def getLast(self):
        if len(self.moves) == 0:
            return [False]
        else:
            return [True, self.moves[-1]]

    def getAll(self):
        return self.moves