from cell import Cell
from line import Line
from point import Point
from window import Window

win = Window(800, 600)

top_left = Point(0,0)
bottom_right = Point(10,10)
top_left1 = Point(10,0)
bottom_right1 = Point(20,10)
top_left20 = Point(40,40)
bottom_right20 = Point(50,50)
cells = []
cell1 = Cell(True, True, True, False, top_left, bottom_right, win)
cell2 = Cell(True, False, True, True, top_left1, bottom_right1, win)
cell20 = Cell(True, False, True, True, top_left20, bottom_right20, win)
cells.append(cell1)
cells.append(cell2)
cells.append(cell20)
for cell in cells:
    cell.draw()

win.wait_for_close()