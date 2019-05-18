"""Create a canvas and add lines and rectangles."""

import tkinter as tk
from tklib import *

class Demo(App):
    def __init__(self):
        super(Demo, self).__init__()
        Label("Canvas", font="Arial 24")
        c = Canvas(600, 300)
        c.create_line(10, 10, 200, 200, fill='red')
        c.create_line(20, 10, 210, 200, fill='blue', width=3)
        c.create_rectangle(100, 200, 150, 250, fill='green', width=2)
        c.create_rectangle(300, 100, 580, 250, fill='yellow', width=5)

if __name__ == '__main__':
    Demo().run()