"""Place polygons on the canvas."""
from tklib import *

class Demo(App):
    def __init__(self):
        super(Demo, self).__init__()
        Label("Polygons", font="Arial 24")
        self.c = Canvas(600, 300)
        self.c.polygon(150, 150, 100, 6, fill='blue')
        self.c.polygon(450, 150, 80, 8, fill='red', width=5)

if __name__ == '__main__':
    Demo().run()