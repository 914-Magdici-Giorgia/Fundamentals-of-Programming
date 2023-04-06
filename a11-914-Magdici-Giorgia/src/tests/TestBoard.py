import unittest
from src.board.board import Board

class TestBoard(unittest.TestCase):
    def setUp(self) -> None:
        self._board = Board(15)

    def test_get_board(self):
        self.assertEqual(self._board.board, 15)

    def test_move_raise_exceptions(self):
        with self.assertRaises(Exception) as exc:
            self._board.moves(30, 20, "○")
        self.assertEqual(str(exc.exception), "Not a valid cell!")

    def test_check(self):
        self.assertEqual(self._board.check("○", "○", "○", "○", "○", "○"), True)
