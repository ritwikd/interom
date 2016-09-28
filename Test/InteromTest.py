import unittest, AlgNote, DoMove, ValidMove

unit_tests = []

unit_tests.append(AlgNote.AlgNoteTest)
unit_tests.append(DoMove.DoMoveTest)
unit_tests.append(ValidMove.ValidMoveTest)

for test in unit_tests:
    suite = unittest.TestLoader().loadTestsFromTestCase(test)
    unittest.TextTestRunner.run(suite)