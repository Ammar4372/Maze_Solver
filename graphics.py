from tkinter import Tk,BOTH,Canvas

class Window:
    def __init__(self, width: int, height: int) -> None:
        self.__root = Tk()
        self.__root.title = "Maze Solver"
        self.canvas = Canvas(bg="Black", height=height, width=width)
        self.canvas.pack(fill=BOTH, expand=1)
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW",self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
        
    def close(self):
        self.running = False