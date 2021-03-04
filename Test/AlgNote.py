import unittest, Game

class AlgNoteTest(unittest.TestCase):

    def setUp(self):
        self.board = Game.Board.Board()
        self.board.set_start_pos()

    def test_take(self):
        print('Testing algebraic notation implementation for: TAKE')
        self.assertEqual(True, False)

    def test_castle_queenside(self):
        print('Testing algebraic notation implementation for: CASTLING QUEENSIDE')
        self.assertEqual(True, False)

    def test_castle_kingside(self):
        print('Testing algebraic notation implementation for: CASTLING KINGSIDE')
        self.assertEqual(True, False)

    def test_rook_conflict(self):
        print('Testing algebraic notation implementation for: ROOK CONFLICT')
        self.assertEqual(True, False)

    def test_knight_conflict(self):
        print('Testing algebraic notation implementation for: KNIGHT CONFLICT')
        self.assertEqual(True, False)

    def test_check(self):
        print('Testing algebraic notation implementation for: CHECK')
        self.assertEqual(True, False)

    def test_mate(self):
        print('Testing algebraic notation implementation for: CHECKMATE')
        self.assertEqual(True, False)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AlgNoteTest)
    unittest.TextTestRunner(verbosity=1).run(suite)