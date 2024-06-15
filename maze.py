from cell import Cell
import time
import random

class Maze:
    def __init__(self, rows, cols, cell_size, win=None, origin=[0,0], seed=None) -> None:
        self.grid = []
        self.win = win
        self.cell_size = cell_size
        self.rows = rows
        self.cols = cols
        self.origin = origin
        if not seed:
            self.seed = random.seed(seed)
        else:
            self.seed = 150
        self._create_cells()
        self._break_entrance_and_exit()
        self.break_walls_r(0,0)
        self.reset_visited()

    def _create_cells(self):
        for i in range(self.cols):
            self.grid.append([])
            for j in range(self.rows):
                x1 = (i * self.cell_size) + self.origin[0]
                x2 = x1 + self.cell_size
                y1 = (j * self.cell_size) + self.origin[1]
                y2 = y1 + self.cell_size
                self.grid[i].append(Cell(x1,y1,x2,y2,self.win.canvas))
        self._animate()

    def _animate(self):
        self.win.redraw()
        time.sleep(.05)

    def _break_entrance_and_exit(self):
        entrance = self.grid[0][0]
        exit = self.grid[-1][-1]
        if bool(random.getrandbits(1)):
            entrance.up_wall = False
        else:
            entrance.left_wall = False
        if bool(random.getrandbits(1)):
            exit.down_wall = False
        else:
            exit.right_wall = False
        entrance.draw(entrance.x1,entrance.y1,entrance.x2,entrance.y2)
        exit.draw(exit.x1,exit.y1,exit.x2,exit.y2)

    def break_walls_r(self, i, j):
        self.grid[i][j].visited = True
        while True:
            to_visit = []
            if j > 0 and not self.grid[i][j-1].visited:
                to_visit.append((i, j-1))
            if i < self.cols - 1 and not self.grid[i+1][j].visited:
                to_visit.append((i+1, j))
            if i > 0 and not self.grid[i-1][j].visited:
                to_visit.append((i-1, j))
            if j < self.rows - 1 and not self.grid[i][j+1].visited:
                to_visit.append((i, j+1))
            
            if not to_visit:
                current = self.grid[i][j]
                current.draw(current.x1, current.y1, current.x2, current.y2)
                return
            else:
                to_cell = random.choice(to_visit)
                to_i, to_j = to_cell

                current = self.grid[i][j]
                next_cell = self.grid[to_i][to_j]

                if to_i > i:
                    current.right_wall = False
                    next_cell.left_wall = False
                elif to_i < i:
                    current.left_wall = False
                    next_cell.right_wall = False
                elif to_j > j:
                    current.down_wall = False
                    next_cell.up_wall = False
                elif to_j < j:
                    current.up_wall = False
                    next_cell.down_wall = False

                self.break_walls_r(to_i, to_j)

    def reset_visited(self):
        for col in self.grid:
            for row in col:
                row.visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        current = self.grid[i][j]
        current.visited = True
        if i == self.cols -1 and j == self.rows -1:
            return True
        if i < self.cols - 1 and not current.right_wall and not self.grid[i+1][j].visited:
            current.draw_move(self.grid[i+1][j])
            if self._solve_r(i+1, j):
                return True
            else:
                current.draw_move(self.grid[i+1][j], True)
        if i > 0 and not current.left_wall and not self.grid[i-1][j].visited:
            current.draw_move(self.grid[i-1][j])
            if self._solve_r(i-1, j):
                return True
            else:
                current.draw_move(self.grid[i-1][j], True)
        if j < self.rows - 1 and not current.down_wall and not self.grid[i][j+1].visited:
            current.draw_move(self.grid[i][j+1])
            if self._solve_r(i, j+1):
                return True
            else:
                current.draw_move(self.grid[i][j+1], True)
        if j > 0 and not current.up_wall and not self.grid[i][j-1].visited:
            current.draw_move(self.grid[i][j-1])
            if self._solve_r(i, j-1):
                return True
            else:
                current.draw_move(self.grid[i][j-1], True)
        else:
            return False