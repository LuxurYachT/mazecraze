from tkinter import Tk, BOTH, Canvas

class Window:

    def __init__(self, width, height) -> None:
        self.root = Tk()
        self.root.title = "window"
        self.canvas = Canvas(self.root, width=width, height=height)
        self.canvas.pack()
        self.is_running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()


    def wait_for_close(self):
        self.is_running = True
        while self.is_running:
            self.redraw()

    def close(self):
        self.is_running = False

    def draw_line(self, line, color):
        line.draw(self.canvas, color)