import unittest
from src.ai.ai import AI
from src.board.board import Board


class TestAi(unittest.TestCase):
    def setUp(self) -> None:
        self._ai = AI()
        self._board = Board(15)

    def test_check(self):
        self.assertEqual(self._ai.check(Board(15), self._board.data), False)

    def test_canwin(self):
        self.assertEqual(self._ai.canwin(Board(15), self._board.data), False)
        self._board.data[1][3] = '●'
        b = Board(15)
        self.assertEqual(self._ai.canwin(b, self._board.data), False)



