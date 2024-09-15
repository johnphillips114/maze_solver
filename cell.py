from line import Line
from point import Point

class Cell:
    def __init__(
            self, 
            has_left_wall, 
            has_right_wall, 
            has_top_wall, 
            has_bottom_wall,
            top_left,
            bottom_right,
            win,
        ):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = top_left.x
        self._x2 = bottom_right.x
        self._y1 = top_left.y
        self._y2 = bottom_right.y
        self._win = win

    def draw(self, top_left=None, bottom_right=None):
        if not top_left:
            top_left = Point(self._x1, self._y1)
        if not bottom_right:
            bottom_right = Point(self._x2, self._y2)
        start_point = Point(top_left.x, top_left.y)
        end_point = Point(top_left.x, bottom_right.y)
        line = Line(start_point, end_point)
        if self.has_left_wall:
            color = "black"
        else:
            color = "#d9d9d9"
        self._win.draw_line(line, color)
        
        start_point = Point(top_left.x, top_left.y)
        end_point = Point(bottom_right.x, top_left.y)
        line = Line(start_point, end_point)
        if self.has_top_wall:
            color = "black"
        else:
            color = "#d9d9d9"
        self._win.draw_line(line, color)

        start_point = Point(bottom_right.x, top_left.y)
        end_point = Point(bottom_right.x, bottom_right.y)
        line = Line(start_point, end_point)
        if self.has_right_wall:
            color = "black"
        else:
            color = "#d9d9d9"
        self._win.draw_line(line, color)

        start_point = Point(top_left.x, bottom_right.y)
        end_point = Point(bottom_right.x, bottom_right.y)
        line = Line(start_point, end_point)
        if self.has_bottom_wall:
            color = "black"
        else:
            color = "#d9d9d9"
        self._win.draw_line(line, color)

    def draw_move(self, to_cell, undo=False):
        if undo:
            color = "red"
        else:
            color = "gray"
        from_cell_center = self.get_cell_center()
        to_cell_center = to_cell.get_cell_center()
        line = Line(from_cell_center, to_cell_center)
        self._win.draw_line(line, color)

    def get_cell_center(self):
        return Point((self._x1+self._x2)/2, (self._y1+self._y2)/2)