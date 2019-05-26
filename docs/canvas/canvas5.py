"""Place random circles on the canvas."""
from tklib import *
import random

class Demo(App):
    def __init__(self): 
        super(Demo, self).__init__()
        Label("Random Circles", font="Arial 24")

        w, h = 600, 300
        c = Canvas(width=w, height=h, background='lightblue')
        
        for i in range(50):
            x = random.randint(0, w)
            y = random.randint(0, h)
            r = random.randint(10, 100)
            c.create_oval(x, y, x+r, y+r)

if __name__ == '__main__':
    Demo().run()