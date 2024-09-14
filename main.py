from line import Line
from point import Point
from window import Window

win = Window(800, 600)
start_point = Point(1,1)
end_point = Point(20,60)
line1 = Line(
    start_point,
    end_point,
)
win.draw_line(line1, fill_color="red")
print(win.debug_print())
win.wait_for_close()