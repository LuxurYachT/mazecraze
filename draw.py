class Point:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


class Line:

    def __init__(self, p1, p2) -> None:
        self.p1 = p1
        self.p2 = p2
        self.line_thick = 3

    def draw(self, canvas, color):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=color, width=self.line_thick)
