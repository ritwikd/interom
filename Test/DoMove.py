import unittest, Game

P = Game.Position.Position

class DoMoveTest(unittest.TestCase):

    def setUp(self):
        self.board = Game.Board.Board()
        self.board.set_start_pos()

    def test_queen(self):
        print 'Testing do_move implementation for: QUEEN'

    def test_rook(self):
        print 'Testing do_move implementation for: ROOK'

    def test_knight(self):
        print 'Testing do_move implementation for: KNIGHT'

    def test_bishop(self):
        print 'Testing do_move implementation for: BISHOP'

    def test_king(self):
        print 'Testing do_move implementation for: KING'

    def test_pawn(self):
        print 'Testing do_move implementation for: PAWN'
        result = self.board.do_move(P(0,1), P(0,3))
        self.assertEqual(result, True)

        result = self.board.do_move(P(0,3), P(0,4))
        self.assertEqual(result, True)

        result = self.board.do_move(P(1,6), P(1,4))
        self.assertEqual(result, True)

        result = self.board.do_move(P(0,4), P(1,5))
        self.assertEqual(result, True)

        result = self.board.do_move(P(1,1), P(1,2))
        self.assertEqual(result, True)

        result = self.board.do_move(P(2,1), P(2,4))
        self.assertEqual(result, False)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(DoMoveTest)
    unittest.TextTestRunner(verbosity=2).run(suite)