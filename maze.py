from cell import Cell
from point import Point
from window import Window

import random
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
            seed = None,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = [[]*self.num_rows]*self.num_cols
        if seed != None:
            self.seed = random.seed(seed)

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
        for i in range(0, self.num_cols):
            for j in range(0, self.num_rows):
                self._break_walls_r(i, j)

            
    
    def _animate(self):
        while self.win.is_running:
            sleep(0.5)
            self.win.redraw()
            
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

    def _break_walls_r(self, i, j):
        print(f"Starting break_walls_r at {i}, {j}")
        self._cells[i][j].visited = True
        need_to_visit = []
        adjacent_cells = self._get_adjacent_cells(i, j)
        print(f"adjacent cells: {adjacent_cells}")
        for adjacent_cell in adjacent_cells:
            if adjacent_cell == None:
                continue
            print(f"One of the adjacent cells: {adjacent_cell}")
            print(f"Has it been visited: {self._cells[adjacent_cell[0]][adjacent_cell[1]].visited}")
            if self._cells[adjacent_cell[0]][adjacent_cell[1]].visited == False:
                need_to_visit.append(adjacent_cell)
        if need_to_visit == []:
            self._cells[i][j].draw()
            return
        if i == 0:
            print(f"in ({i}, {j}) - Need to visit these cells: {need_to_visit}")
        rand_direction = random.randrange(0,len(adjacent_cells))
        while adjacent_cells[rand_direction] == None:
            rand_direction = random.randrange(0,len(adjacent_cells))

        
        # break down right side
        if rand_direction == 0:
            self._cells[i][j].has_right_wall = False
            self._cells[i][j].draw()
            if i < self.num_cols - 1:
                target_cell = self._cells[i+1][j]
                target_cell.has_left_wall = False
                target_cell.draw()
        # break down left side
        if rand_direction == 1:
            self._cells[i][j].has_left_wall = False
            self._cells[i][j].draw()
            if i > 0:
                target_cell = self._cells[i-1][j]
                target_cell.has_right_wall = False
                target_cell.draw()
        # break down bottom
        if rand_direction == 2:
            self._cells[i][j].has_bottom_wall = False
            self._cells[i][j].draw()
            if j < self.num_rows - 1:
                target_cell = self._cells[i][j-1]
                target_cell.has_top_wall = False
                target_cell.draw()
        # break down top
        if rand_direction == 3:
            self._cells[i][j].has_top_wall = False
            self._cells[i][j].draw()
            if j > 0:
                target_cell = self._cells[i][j+1]
                target_cell.has_bottom_wall = False
                target_cell.draw()
        self._animate()
        
        self._break_walls_r(adjacent_cells[rand_direction][0], adjacent_cells[rand_direction][1])
        self._reset_cells_visited()
        

    def _get_adjacent_cells(self, i, j):
        adjacent_cells = [None]*4
        # check to see if we're in the left-most column
        if i > 0:
            adjacent_cells[0] = (i - 1, j)
        # check to see if we're in the right-most column
        if i < self.num_cols - 1:
            adjacent_cells[1] = (i + 1, j)
        # check to see if we're in the top row
        if j > 0:
            adjacent_cells[2] = (i, j - 1)
        # check to see if we're in the bottom
        if j < self.num_rows - 1:
            adjacent_cells[3] = (i, j + 1)
                
        return adjacent_cells

    
    def _reset_cells_visited(self):
        for column in self._cells:
            for cell in column:
                if cell.visited == True:
                    print(f"visited: {cell.visited} top-left: {cell._x1}, {cell._y1} - bottom-right: {cell._x2}, {cell._y2}")
                cell.visited = False