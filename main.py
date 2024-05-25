from graphics import Window
from maze import Maze
def main():
    win = Window(800,800)
    Maze(20,20,19,19,40,40,win)
    win.wait_for_close()

main()