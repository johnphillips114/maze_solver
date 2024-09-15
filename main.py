from maze import Maze
from window import Window

win = Window(1200, 800)

num_cols = 12
num_rows = 10
m1 = Maze(0, 0, num_rows, num_cols, 30, 30, win)

win.wait_for_close()