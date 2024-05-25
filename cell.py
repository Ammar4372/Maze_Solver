from graphics import Line,Point
class Cell:
    def __init__(self, win:object) -> None:
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self.has_left_wall = True

    def draw(self, x1:int, y1:int, x2:int, y2:int)-> None:
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1,y2),Point(x1,y1))
            self._win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(x1,y1),Point(x2,y1))
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x2,y1),Point(x2,y2))
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(x2,y2),Point(x1,y2))
            self._win.draw_line(line)
    def draw_move(self, to_cell:object,undo=False) -> None:
        fill_color = "red"
        if undo:
            fill_color = "gray"
        half_length = abs(self._x2 - self._x1) // 2
        x_center = half_length + self._x1
        y_center = half_length + self._y1

        half_length2 = abs(to_cell._x2 - to_cell._x1) // 2
        x_center2 = half_length2 + to_cell._x1
        y_center2 = half_length2 + to_cell._y1
        self._win.draw_line(Line(Point(x_center,y_center),Point(x_center,y_center)),fill_color)