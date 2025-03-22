import random


class Cell:
    def __init__(self, arround_mines=0, mine=False):
        self.arround_mines = arround_mines
        self.mine = mine
        self.fl_open = False


class GamePole:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.pole = [[Cell() for i in range(N) for j in range(N)]]
        self.init()

    def init(self):
        min_pl = 0
        while min_pl < self.M:
            x = random.randint(0, self.N)
            y = random.randint(0, self.N)
            if not self.pole[x][y].mine:
                self.pole[x][y].mine = True
                min_pl += 1
                self.upd_arr_min(x, y)

    def upd_arr_min(self, x, y):
        for i in range(max(0, x - 1), min(self.N, x + 2)):
            for j in range(max(0, y - 1), min(self.N, y + 2)):
                if not (i == x and j == y) and self.pole[i][j].mine:
                    self.pole[i][j].arround_mines += 1
