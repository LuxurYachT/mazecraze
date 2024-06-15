from draw import Point, Line

class Cell:
    def __init__(self, x1, y1, x2, y2, window=None) -> None:
        self.left_wall = True
        self.right_wall = True
        self.up_wall = True
        self.down_wall = True
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.win = window
        self.visited = False
        self.draw(self.x1, self.y1, self.x2, self.y2)

    def draw(self, x1, y1, x2, y2):
        wall = Line(Point(x1,y1), Point(x1,y2))
        if self.left_wall:
            wall.draw(self.win, "black")
        else:
            wall.draw(self.win, "white")
        wall = Line(Point(x2,y1), Point(x2,y2))        
        if self.right_wall:
            wall.draw(self.win, "black")
        else:
            wall.draw(self.win, "white")
        wall = Line(Point(x1,y1), Point(x2,y1))
        if self.up_wall:
            wall.draw(self.win, "black")
        else:
            wall.draw(self.win, "white")
        wall = Line(Point(x1,y2), Point(x2,y2))
        if self.down_wall:
            wall.draw(self.win, "black")
        else:
            wall.draw(self.win, "white")

    def draw_move(self, to_cell, undo=False):
        color = "red"
        if undo:
            color = "gray"
        start = [(self.x1 + self.x2)/2, (self.y1 + self.y2)/2]
        end = [(to_cell.x1 + to_cell.x2)/2, (to_cell.y1 + to_cell.y2)/2]
        path = Line(Point(start[0], start[1]), Point(end[0], end[1]))
        path.draw(self.win, color)