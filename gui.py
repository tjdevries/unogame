from Tkinter import *
from Canvas import Rectangle, CanvasText, Group, Window

#Bugfix
class Group(Group):
    def bind(self, sequence=None, command=None):
        return self.canvas.tag_bind(self.id, sequence, command)

CARDWIDTH = 100
CARDHEIGHT = 150
MARGIN = 10
XSPACING = CARDWIDTH + 2*MARGIN
YSPACING = CARDHEIGHT + 4*MARGIN
OFFSET = 5

BACKGROUND = '#070'
