from graphics import Window
from cell import Cell

def main():
    win = Window(800,800)
    c = Cell(win)
    c.draw(300, 300, 500, 500)
    c1= Cell(win)
    c1.draw(500,300,700,550)
    c.draw_move(c1,True)
    win.wait_for_close()

main()