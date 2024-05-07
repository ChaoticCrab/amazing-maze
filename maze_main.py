from maze_graphics import Window
from maze_maze import Maze
import sys

def main():
    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows

    sys.setrecursionlimit(10000)
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    print("Maze created")
    is_solvable = maze.solve()
    if not is_solvable:
        print("It cannot be solved!")
    else:
        print("Maze solved!")

    win.wait_for_close()

main()

# line1 = Line(Point(100,100), Point(400, 400))
# line2 = Line(Point(100,100), Point(100, 200))
# line3 = Line(Point(100,100), Point(200, 100))
# line4 = Line(Point(100,100), Point(200, 800))
# win.draw_line(line1, "blue")
# win.draw_line(line2, "blue")
# win.draw_line(line3, "blue")
# win.draw_line(line4, "blue")

# c1 = Cell(win)
# c1.has_left_wall = False
# c1.draw(50, 50, 100, 100)

# c2 = Cell(win)
# c2.has_top_wall = False
# c2.draw(150, 50, 200, 100)

# c3 = Cell(win)
# c3.has_bottom_wall = False
# c3.draw(250,50, 300, 100)

# c4 = Cell(win)
# c4.has_right_wall = False
# c4.draw(350, 50, 400, 100)

# c1.draw_move(c2)
# c2.draw_move(c3)
# c3.draw_move(c4, True)

