from texttable import Texttable


class Board:
    def __init__(self):
        self._data=[[0 for j in range (7)] for i in range (7)]
        self._set_element(3,3,'E')

    def __str__(self):          #cu x ascunsi
        t = Texttable()     #initializam Texttable

        header_row = ['/']
        for i in range(1, 8):
            header_row.append(chr(64 + i))          #construim o lista cu elementele din "header"    / A  B  C ....


        t.header(header_row)        #o punem in tabel cu metode specifice modulului texttable


        for i in range(7):
            display_row = [i+1]     #construim o linie noua, punem elementele din acea linie intr-o lista (mai intai numarul liniei)
            for j in range(7):
                element = self._data[i][j]
                if element == 0 or element == 'X':
                    display_row.append(' ')     #apoi fiecare element din lista (daca e 0 sau X jucatorul nu vede nimic in acel patratel
                else:
                    display_row.append(element)     #daca e orice altceva jucatorul vede elementul)
            t.add_row(display_row)      #lipim noua linie la texttable
        return t.draw()     #se returneaza texttable in versiunea mai pretty

    def _str_cheat(self):
        t = Texttable()
        header_row = ['/']
        for i in range(1, 8):
            header_row.append(chr(64 + i))
        t.header(header_row)
        for i in range(7):
            display_row = [i + 1]
            for j in range(7):
                element = self._data[i][j]
                if element == 0 :
                    display_row.append(' ')
                else:
                    display_row.append(element)
            t.add_row(display_row)
        return t.draw()

    def __getitem__(self,x,y):
        return self._data[x][y]

    def _set_element(self,x,y,symbol):
        self._data[x][y]=symbol

    @staticmethod
    def _inboard(x, y):
        if not (0 <= x <= 6 and 0 <= y <= 6):
            return False
        return True

    def _adjacent(self, x, y, symbol):
        """
        checks if the element from coordinates(x,y) is adjacent with a <<symbol>>
        """
        dx = [-1, -1, -1, 0, 1, 1, 1, 0]
        dy = [-1, 0, 1, 1, 1, 0, -1, -1]
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if self._inboard(nx, ny) and self._data[nx][ny] == symbol:
                return True
        return False



