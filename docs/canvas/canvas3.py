"""Painting with ovals."""
from tklib import *

class Demo(App):
    def __init__(self):
        super().__init__()
        Label("Painting using ovals", font="Arial 24")
        self.c = Canvas(width=600, height=300, background='lightblue')
        self.c.bind('<B1-Motion>', self.paint)

    def paint(self, event):
        """Draw ovals on the canvas."""
        x0, y0 = event.x-1, event.y-1
        x1, y1 = event.x+1, event.y+1
        self.c.create_oval(x0, y0, x1, y1, fill='blue')

Demo().run()