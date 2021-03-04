import unittest, Game

class CheckTest(unittest.TestCase):

    def setUp(self):
        self.board = Game.Board.Board()

    def test_basic(self):
        P = Game.Position.Position
        K = Game.Pieces.Other.King.King
        Q = Game.Pieces.Major.Queen.Queen

        print('Testing board check implementation: BASIC')


        K_w = K(self.board, P(4,0), True)
        K_b = K(self.board, P(4,7), False)

        Q_w = Q(self.board, P(0,0), True)
        Q_b = Q(self.board, P(0,7), False)

        self.board.set_piece(K_w.P_c, K_w)
        self.board.set_piece(K_b.P_c, K_b)
        self.board.set_piece(Q_w.P_c, Q_w)
        self.board.set_piece(Q_b.P_c, Q_b)

        self.board.do_move(P(0,7), P(1,7))

        result = self.board.do_move(P(0,0), P(4,4))
        self.assertEqual(result, True)

        result = self.board.check_any()
        self.assertEqual(result['b'], True)

        result = self.board.do_move(P(1,7), P(4,4))
        self.assertEqual(result, True)

        result = self.board.check_any()
        self.assertEqual(result['w'], True)

        result = self.board.do_move(P(4,4), P(0,4))
        self.assertEqual(result, True)

        result = self.board.check_any()
        self.assertEqual(result['w'], True)

    def test_pins(self):
        P = Game.Position.Position
        K = Game.Pieces.Other.King.King
        Q = Game.Pieces.Major.Queen.Queen

        print('Testing board check implementation: PINS')

        K_w = K(self.board, P(4, 0), True)
        K_b = K(self.board, P(4, 7), False)

        Q_w = Q(self.board, P(4, 1), True)
        Q_b = Q(self.board, P(4, 6), False)

        self.board.set_piece(K_w.P_c, K_w)
        self.board.set_piece(K_b.P_c, K_b)
        self.board.set_piece(Q_w.P_c, Q_w)
        self.board.set_piece(Q_b.P_c, Q_b)

        result = self.board.do_move(P(4,1), P(4,2))
        self.assertEqual(result, True)

        result = self.board.do_move(P(4,2), P(3,3))
        self.assertEqual(result, False)

        result = self.board.do_move(P(4,2), P(4,6))
        self.assertEqual(result, True)

        result = self.board.check_any()
        self.assertEqual(result['b'], True)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(CheckTest)
    unittest.TextTestRunner(verbosity=1).run(suite)

