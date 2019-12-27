"""Base your program on this template."""

import tkinter as tk
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

if __name__ == '__main__':
    Demo().run()