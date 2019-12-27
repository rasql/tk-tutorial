"""Base your program on this template."""
from tklib import *

def callback(event):
    print(event)

class Demo(App):
    def __init__(self):
        super().__init__()
        Label('Template', font='Arial 24')

        Frame()
        Button()
        Label()
        Entry()

Demo().run()