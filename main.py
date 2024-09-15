from maze import Maze
from window import Window

win = Window(1200, 800)

num_cols = 2
num_rows = 3
m1 = Maze(10, 10, num_rows, num_cols, 20, 20, win)

win.wait_for_close()