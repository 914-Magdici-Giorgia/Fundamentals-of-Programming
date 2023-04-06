from texttable import Texttable


class Board:
    def __init__(self, size):
        self.__board = size
        self.__data = [[0 for j in range(self.__board)] for i in range(self.__board)]

    @property
    def board(self):
        return self.__board

    @property
    def data(self):
        return self.__data

    def move(self, square, symbol):
        """
        Turn square into coordinates
        :param square: the coordinates
        :param symbol: black or white
        """
        col = ord(square[0]) - 65
        row = int(square[1:])
        self.moves(row, col, symbol)
        pass

    def moves(self, x, y, symbol):
        """
        Put the move on the board
        :param x: row
        :param y: col
        :param symbol: black or white
        """
        if not (0 <= x < self.__board and 0 <= y < self.__board):
            raise Exception("Not a valid cell!")

        if self.__data[x][y] != 0:
            raise Exception("Piece already exists in this position!")

        if self.__data[x][y] == 0:
            self.__data[x][y] = symbol

    def empty_squares(self):
        """
        :return: result
        """
        result = []
        for i in range(self.__board):
            for j in range(self.__board):
                if self.__data[i][j] == 0:
                    result.append((i, j))
        return result

    @staticmethod
    def check(d1, d2, d3, d4, d5, symbol):
        """

        :param d1, d2, d3, d4, d5: 5 cells
        :param symbol: black or white
        :return: true or false
        """
        if d1 == d2 == d3 == d4 == d5 == symbol:
            return True
        else:
            return False

    def checkwin(self):
        """
        Winning or losing judgment
        :return: true or false
        """
        for i in range(self.__board):
            for j in range(self.__board):
                horizontal_white = self.check(self.__data[i][j - 4], self.__data[i][j - 3], self.__data[i][j - 2],
                                              self.__data[i][j - 1], self.__data[i][j], "●")
                vertical_white = self.check(self.__data[i - 4][j], self.__data[i - 3][j], self.__data[i - 2][j],
                                            self.__data[i - 1][j], self.__data[i][j], "●")
                # check for diagonal from right to left (top right - left bottom and the opposite)
                trl_diagonal_white = self.check(self.__data[i - 4][j - 4], self.__data[i - 3][j - 3],
                                                self.__data[i - 2][j - 2],
                                                self.__data[i - 1][j - 1], self.__data[i][j], "●")
                # check for diagonal from left to right (top left - right bottom and the opposite)
                tlr_diagonal_white = self.check(self.__data[i][j - 4], self.__data[i - 1][j - 3],
                                                self.__data[i - 2][j - 2],
                                                self.__data[i - 3][j - 1], self.__data[i - 4][j], "●")
                horizontal_black = self.check(self.__data[i][j - 4], self.__data[i][j - 3], self.__data[i][j - 2],
                                              self.__data[i][j - 1], self.__data[i][j], "○")
                vertical_black = self.check(self.__data[i - 4][j], self.__data[i - 3][j], self.__data[i - 2][j],
                                            self.__data[i - 1][j], self.__data[i][j], "○")
                # check for diagonal from right to left (top right - left bottom and the opposite)
                trl_diagonal_black = self.check(self.__data[i - 4][j - 4], self.__data[i - 3][j - 3],
                                                self.__data[i - 2][j - 2],
                                                self.__data[i - 1][j - 1], self.__data[i][j], "○")
                # check for diagonal from left to right (top left - right bottom and the opposite)
                tlr_diagonal_black = self.check(self.__data[i][j - 4], self.__data[i - 1][j - 3],
                                                self.__data[i - 2][j - 2],
                                                self.__data[i - 3][j - 1], self.__data[i - 4][j], "○")
                if horizontal_white or horizontal_black or vertical_black or vertical_white or tlr_diagonal_black or \
                        tlr_diagonal_white or trl_diagonal_black or trl_diagonal_white:
                    return True
        return False

    def __str__(self):
        """
         Initialize header
        :return:
        """
        t = Texttable()

        # Horizontal header
        header_row = ['/']
        for i in range(self.__board):
            header_row.append(chr(65 + i))
        t.header(header_row)

        for i in range(self.__board):
            row = self.__data[i]
            # Initialize vertical header
            display_row = [i]

            for j in range(self.__board):
                val = self.__data[i][j]
                if val == 0:
                    display_row.append(' ')
                else:
                    display_row.append(val)

            t.add_row(display_row)
        return t.draw()
