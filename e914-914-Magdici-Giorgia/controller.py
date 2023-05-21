import random

from board import Board


class PositionError(Exception):
    pass


class Controller:
    def __init__(self,board):
        self._board=board
        self._aliens=[]



    def _random_position(self):
        while True:
            x=random.randint(0,6)
            y=random.randint(0,6)
            if self._board._data[x][y]==0:
                return [x,y]


    def _random_asteroids(self):
        count=0
        while count<8:
            x,y=self._random_position()
            if not self._board._adjacent(x,y,'*'):
                self._board._set_element(x,y,'*')
                count+=1


    def _random_aliens(self, nr, dist):
        count = 0
        frame=[dist, 6 - dist]
        while count < nr:
            x, y = self._random_position()
            if x in frame or y in frame:
                self._board._set_element(x, y, 'X')
                self._aliens.append([x,y,dist])
                count += 1



    def _normal_board(self):
        return self._board

    def _cheat_board(self):
        return self._board._str_cheat()

    def _remove_aliens(self):
        "deletes the aliens from the board"
        for i in range(7):
            for j in range(7):
                if self._board._data[i][j]=='X':
                    self._board._set_element(i,j,0)

    def _reposition_aliens(self):
        "finds a new place for the aliens"
        for i in range(len(self._aliens)):
            x=self._aliens[i][0]
            y=self._aliens[i][1]
            if self._board._data[x][y]=='-':
                self._aliens.pop(i)


        for i in range(len(self._aliens)):
            distance=random.randint(0,1)
            alien=self._aliens[i]
            # self._random_aliens(1,alien[2]+distance)
            # self._aliens.pop(i)
            i+=1


    def won(self):
        if len(self._aliens)==0:
            return True
        return False

    def lost(self):
        for i in range(len(self._aliens)):
            alien = self._aliens[i]
            if self._board._adjacent(alien[0],alien[1],'E')==True
                return True
        return False


    def _fire(self,x,y):
        """
        sees what is on the fired position and calls the needed function
        """
        if self._board._data[x][y]=='*' or self._board._data[x][y]=='-':
            raise PositionError("There is just an asteroid or the ashes of an alien ship.")
        else:
            if self._board._data[x][y]=='X':
                self._hit(x,y)
            else:
                self._remove_aliens()
                self._reposition_aliens()
                raise PositionError("you missed")




    def _hit(self,x,y):
        "deletes the fired alien and replaces the other one"
        self._board._set_element(x, y, '-')
        self._remove_aliens()  # only from board
        self._reposition_aliens()






# b=Board()
# c=Controller(b)
# c._random_asteroids()
# c._random_aliens(2,0)
# print(c._board._str_cheat())
