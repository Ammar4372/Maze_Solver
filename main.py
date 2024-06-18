from graphics import Window
from maze import Maze


def main():
    win = Window(800, 800)
    maze = Maze(40, 40, 9, 9, 80, 80, win, 0)
    maze.solve()
    win.wait_for_close()


main()
