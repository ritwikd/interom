import unittest, Game

class ValidMoveTest(unittest.TestCase):

    def setUp(self):
        self.board = Game.Board.Board()
        self.board.set_start_pos()

    def test_queen(self):
        print('Testing valid_move implementation for: QUEEN')
        self.assertEqual(True, False)

    def test_rook(self):
        print('Testing valid_move implementation for: ROOK')
        self.assertEqual(True, False)

    def test_knight(self):
        print('Testing valid_move implementation for: KNIGHT')
        self.assertEqual(True, False)

    def test_bishop(self):
        print('Testing valid_move implementation for: BISHOP')
        self.assertEqual(True, False)

    def test_king(self):
        print('Testing valid_move implementation for: KING')
        self.assertEqual(True, False)

    def test_pawn(self):
        print('Testing valid_move implementation for: PAWN')
        self.assertEqual(True, False)



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ValidMoveTest)
    unittest.TextTestRunner(verbosity=1).run(suite)