from board import Board
from controller import Controller, PositionError


class Ui:
    def __init__(self,controller):
        self._controller=controller

    def StartGame(self):
        self._controller._random_asteroids()
        self._controller._random_aliens(2,0)
       # print(self._controller._normal_board())

    def _print_menu(self):
        print("Options:"
              "\n     fire <coordinate>"
              "\n     cheat")

    def play(self):

        self.StartGame()
        while not self._controller.won() and not self._controller.lost():

            print(self._controller._normal_board())
            self._print_menu()

            command=input("your wish:").lower().strip()
            round=0
            if command == 'x':
                return
            if command == 'cheat':
                print(self._controller._cheat_board())
            else:
                word,coordinate=command.split()
                if word =='fire':
                    x=int(coordinate[-2])-1
                    y=ord(coordinate[-1])-97
                    try :
                        self._controller._fire(x,y)
                    except PositionError as pe:
                        print(pe)

                    round=round+1

        if self._controller.won:
            print("CONGRATS! you won")
        else:
            print("you lost :(")







b=Board()
c=Controller(b)
ui=Ui(c)
ui.play()