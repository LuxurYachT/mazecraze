from window import Window
from draw import Point, Line
from cell import Cell
from maze import Maze

win = Window(800, 600)
maze = Maze(12,16,50,win,[10,10])
maze.solve()
win.wait_for_close()