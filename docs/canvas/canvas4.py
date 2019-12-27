"""Place polygons on the canvas."""
from tklib import *

class Demo(App):
    def __init__(self):
        super().__init__()
        Label("Polygons", font="Arial 24")
        self.c = Canvas(width=600, height=300, background='lightblue')
        self.c.polygon(150, 150, 100, 6, fill='blue')
        self.c.polygon(450, 150, 80, 8, fill='red', width=5)

Demo().run()