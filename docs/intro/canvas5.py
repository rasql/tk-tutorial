"""Place random circles on the canvas."""

import tkinter as tk
from tklib import *
import random

class Demo(App):
    def __init__(self): 
        super(Demo, self).__init__()
        Lb("Random Circles", fg="red", font="Arial 24")
        self.c = Can(600, 300)

        w = int(self.c['width'])
        h = int(self.c['height'])
        
        for i in range(50):
            x = random.randint(0, w)
            y = random.randint(0, h)
            r = random.randint(10, 100)
            self.c.create_oval(x, y, x+r, y+r)

if __name__ == '__main__':
    Demo().run()