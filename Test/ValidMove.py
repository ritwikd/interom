import unittest, Game

class ValidMoveTest(unittest.TestCase):

    def setUp(self):
        self.board = Game.Board.Board()
        self.board.set_start_pos()

    def test_rook(self):
        print 'Testing valid_move implementation for: ROOK'
        rookPos = Game.Position.Position(7, 0)
        rookObject = self.board.get_piece(rookPos)[1]
        rookVertMovePos = Game.Position.Position(7, 3)
        self.assertEqual(False, rookObject.valid_move(rookVertMovePos))
        pawnBlockPos = Game.Position.Position(7, 1)
        self.board.set_piece(pawnBlockPos, None)
        self.assertEqual(True, rookObject.valid_move(rookVertMovePos))
        self.board.set_piece(rookVertMovePos, rookObject)
        self.board.set_piece(rookPos, None)
        rookObject.P_c = rookVertMovePos
        rookHorizontalMovePos = Game.Position.Position(0, 3)
        self.assertEqual(True, rookObject.valid_move(rookHorizontalMovePos))
        rookObject.P_c = rookHorizontalMovePos

    def test_bishop(self):
        print 'Testing valid_move implementation for: BISHOP'
        bishopWhiteSquaresPos = Game.Position.Position(5, 0)
        bishopWhiteSquares = self.board.get_piece(bishopWhiteSquaresPos)[1]
        bishopWhiteSquaresMovePos = Game.Position.Position(3, 2)
        pawnBlockBishopWhiteSquares = Game.Position.Position(4, 1)
        self.assertEqual(False, bishopWhiteSquares.valid_move(bishopWhiteSquaresMovePos))
        self.board.set_piece(pawnBlockBishopWhiteSquares, None)
        self.assertEqual(True, bishopWhiteSquares.valid_move(bishopWhiteSquaresMovePos))

        bishopBlackSquaresPos = Game.Position.Position(2, 0)
        bishopBlackSquares = self.board.get_piece(bishopBlackSquaresPos)[1]
        bishopBlackSquaresMovePos = Game.Position.Position(4, 2)
        pawnBlockBishopBlackSquares = Game.Position.Position(3, 1)
        self.assertEqual(False, bishopBlackSquares.valid_move(bishopBlackSquaresMovePos))
        self.board.set_piece(pawnBlockBishopBlackSquares, None)
        self.assertEqual(True, bishopBlackSquares.valid_move(bishopBlackSquaresMovePos))





if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ValidMoveTest)
    unittest.TextTestRunner(verbosity=2).run(suite)