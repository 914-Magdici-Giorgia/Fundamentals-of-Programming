from src.ai.ai import AI
from src.board.board import Board


class UI:
    def __init__(self):
        self.__board = Board(15)
        self.__ai = AI()

    def start(self):
        print("Gomoku!")

        player_turn = True
        while not self.__board.checkwin():
            print(str(self.__board))
            if player_turn:
                try:
                    move = input("Enter your move: ")
                    if move == '0':
                        break
                    self.__board.move(move, '●')
                except Exception:
                    print("Invalid cell spot or cell already taken!")
                    continue
            else:
                ai_move = self.__ai.move(self.__board)
                self.__board.move(ai_move, '○')
                print("Computer moves at: " + str(ai_move))
            player_turn = not player_turn

        if player_turn:
            print("You Lost!")
        else:
            print("You Won!")


ui = UI()
ui.start()
