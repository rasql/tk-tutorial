"""Display tk Text."""

import tkinter as tk
from tklib import *

class Demo(App):
    def __init__(self): 
        super().__init__()
        Label("Spinbox", font="Arial 18")

        self.spinval = tk.StringVar()
        self.spinval.set('10')
        t = ttk.Spinbox(App.stack[-1], from_=5.0, to=100.0, increment=5, textvariable=self.spinval)
        t.grid()

        t = ttk.Spinbox(App.stack[-1], from_=5.0, to=100.0, textvariable=self.spinval)
        t.grid()

if __name__ == '__main__':
    Demo().run()