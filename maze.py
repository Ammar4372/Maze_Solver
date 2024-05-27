from cell import Cell
from time import sleep
import random

class Maze:
    def __init__(self, x:int, y:int, rows:int, cols:int, cell_size_x:int, cell_size_y:int, win=None, seed=None) -> None:
        self._x = x
        self._y = y
        self._rows = rows
        self._cols = cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        if seed is not None:
            random.seed(seed)
        self._create_cels()

    def _create_cels(self)-> None:
        for i in range(self._cols):
            cells_col = []
            for j in range(self._rows):
                c = Cell(self._win)
                cells_col.append(c)
            self._cells.append(cells_col)
        for i in range(self._cols):
            for j in range(self._rows):
                self._draw_cell(i,j)
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()


    def _draw_cell(self, i:int, j: int) -> None:
        if self._win is None:
            return
        x1 = (self._cell_size_x * j) + self._x
        y1 = (self._cell_size_y * i) + self._y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _break_entrance_and_exit(self) -> None:
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[self._cols-1][self._rows-1].has_bottom_wall = False
        self._draw_cell(self._cols-1,self._rows-1)

    def _break_walls_r(self, i:int, j:int) -> None:
        self._cells[i][j].visited = True
        while True:
            adjacent_cells = []
            if i > 0 and not self._cells[i-1][j].visited:
                adjacent_cells.append((i-1,j))
            
            if i < self._cols - 1 and  not self._cells[i+1][j].visited:
                adjacent_cells.append((i+1,j))
            
            if j > 0 and not self._cells[i][j-1].visited:
                adjacent_cells.append((i,j-1))
            
            if j < self._rows-1 and not self._cells[i][j+1].visited:
                adjacent_cells.append((i,j+1))
            
            if len(adjacent_cells) == 0:
                self._draw_cell(i,j)
                return
            
            direction = random.choice(adjacent_cells)
            if direction[0] == i + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i + 1][j].has_top_wall = False

            if direction[0] == i - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i - 1][j].has_bottom_wall = False

            if direction[1] == j + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i][j + 1].has_left_wall = False
            
            if direction[1] == j - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i][j - 1].has_right_wall = False
            
            self._break_walls_r(direction[0],direction[1])
    
    def solve(self):
        return self.solve_r(0,0)
    
    def solve_r(self, i:int,j:int):
        self._animate()
        self._cells[i][j].visited = True
        if i == self._cols-1 and j == self._rows-1:
            return True
        if i > 0 and not self._cells[i-1][j].visited and not self._cells[i-1][j].has_bottom_wall:
            self._cells[i][j].draw_move(self._cells[i-1][j])
            if self.solve_r(i-1,j):
                return True
            self._cells[i][j].draw_move(self._cells[i-1][j],True)
            
        if i < self._cols-1 and not self._cells[i+1][j].visited and not self._cells[i+1][j].has_top_wall:
            self._cells[i][j].draw_move(self._cells[i+1][j])
            if self.solve_r(i+1,j):
                return True
            self._cells[i][j].draw_move(self._cells[i+1][j],True)

        if j > 0 and not self._cells[i][j-1].visited and not self._cells[i][j-1].has_right_wall:
            self._cells[i][j].draw_move(self._cells[i][j-1])
            if self.solve_r(i,j-1):
                return True
            self._cells[i][j].draw_move(self._cells[i][j-1],True)

        if j < self._rows-1 and not self._cells[i][j+1].visited and not self._cells[i][j+1].has_left_wall:
            self._cells[i][j].draw_move(self._cells[i][j+1])
            if self.solve_r(i,j+1):
                return True
            self._cells[i][j].draw_move(self._cells[i][j+1],True)

        return False
    def _reset_cells_visited(self) -> None:
        for i in range(self._cols):
            for j in range(self._rows):
                self._cells[i][j].visited = False
    def _animate(self) -> None:
        if self._win is None:
            return
        self._win.redraw()
        sleep(0.05)

    