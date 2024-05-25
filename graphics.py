from tkinter import Tk,BOTH,Canvas

class Window:
    def __init__(self, width: int, height: int) -> None:
        self.__root = Tk()
        self.__root.title = "Maze Solver"
        self.canvas = Canvas(bg="white", height=height, width=width)
        self.canvas.pack(fill=BOTH, expand=1)
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW",self.close)

    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self) -> None:
        self.running = True
        while self.running:
            self.redraw()
        print("Closing...")
    
    def draw_line(self, line: object, fill_color= "black")-> None:
        line.draw(self.canvas, fill_color)

    def close(self) -> None:
        self.running = False

class Point:
    def __init__(self, x:int, y: int) -> None:
        self.x = x
        self.y = y

class Line:
    def __init__(self,p1: object, p2: object) -> None:
        self.p1 = p1
        self.p2 = p2
    
    def draw(self, canvas: object, fill_color: str) -> None:
        x1 = self.p1.x
        y1 = self.p1.y 
        x2 = self.p2.x 
        y2 = self.p2.y
        canvas.create_line(x1, y1, x2, y2, fill=fill_color, width=2)