import random


class AI:
    def move(self, board):
        """
        non-AI method of making the computer competitive by a small trick
        :param board: the board
        :return: the computer' s move
        """

        letters = [chr(65 + i) for i in range(board.board)]
        digits = [i for i in range(board.board)]
        data = board.data
        if self.check(board, data) and not self.canwin(board, data):
            [letter, digit] = self.check(board, data)
            return chr(65 + digit) + str(letter)
        elif self.canwin(board, data):
            [letter, digit] = self.canwin(board, data)
            if (letter, digit + 1) in board.empty_squares():
                return chr(66 + digit) + str(letter)
            else:
                val = [-1, 0, 1]
                digit += random.choice(val)
                letter += random.choice(val)
                if (letter, digit) in board.empty_squares():
                    return chr(65 + digit) + str(letter)
                else:
                    return random.choice(letters) + str(random.choice(digits))
        return random.choice(letters) + str(random.choice(digits))

    @staticmethod
    def check(board, data):
        directions = ((1, 0), (0, 1), (1, 1), (1, -1))
        for i in range(board.board):
            for j in range(board.board):
                if data[i][j] == 0:
                    continue
                for dir in directions:
                    x, y = i, j
                    count = 0
                    for k in range(5):
                        if x > 14 or x < 0 or y > 14 or y < 0 or data[x][y] == 0:
                            break
                        x += dir[0]
                        y += dir[1]
                        count += 1
                    if (count == 4 or count ==3) and data[i][j] == '●':
                        return [x, y]
        return False

    @staticmethod
    def canwin(board, data):
        for i in range(board.board):
            for j in range(board.board):
                if data[i][j - 3] == data[i][j - 2] == data[i][j - 1] == data[i][j] == '○':
                    return [i, j]
        return False
