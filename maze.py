from cell import Cell
from time import sleep
class Maze:
    def __init__(self, x:int, y:int, rows:int, cols:int, cell_size_x:int, cell_size_y:int, win) -> None:
        self._x = x
        self._y = y
        self._rows = rows
        self._cols = cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cels()

    def _create_cels(self)-> None:
        for i in range(self._rows):
            self._cells.append([])
            for j in range(self._cols):
                c = Cell(self._win)
                self._cells[i].append(c)
                self._draw_cell(i,j)

    def _draw_cell(self, i:int, j: int):
        if self._win is None:
            return
        x1 = (self._cell_size_x * j) + self._x
        y1 = (self._cell_size_y * i) + self._y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):

        self._win.redraw()
        sleep(0.05)