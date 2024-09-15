from cell import Cell
from point import Point
from window import Window

from time import sleep

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = [[]*self.num_rows]*self.num_cols

        self._create_cells()

    def _create_cells(self):
        for i in range(0, self.num_cols):
            for j in range(0, self.num_rows):
                top_left = Point(
                    i * self.cell_size_x + self.x1, 
                    j * self.cell_size_y + self.y1
                )
                bottom_right = Point(
                    i * self.cell_size_x + self.cell_size_x + self.x1, 
                    j * self.cell_size_y + self.cell_size_y + self.y1
                )
                new_cell = Cell(True, True, True, True, top_left, bottom_right, self.win)
                self._cells[i].append(new_cell)
                new_cell.draw()
                self._animate()
        self._break_entrance_and_exit()
            
    
    def _animate(self):
        while self.win.is_running:
            self.win.redraw()
            sleep(0.7)
            
    def _break_entrance_and_exit(self):
        entrance = self._cells[0][0]
        entrance.has_top_wall = False
        entrance.has_left_wall = False
        entrance.draw()
        exit = self._cells[-1][-1]
        exit.has_bottom_wall = False
        exit.has_right_wall = False
        exit.draw()
        print("drew entrance and exit")
        self._animate()