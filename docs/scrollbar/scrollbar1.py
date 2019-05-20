"""Display scrollbars."""

import tkinter as tk
import tkinter.ttk as ttk
from tklib import *

class Demo(App):
    def __init__(self): 
        super(Demo, self).__init__()
        Label("Scrollbars", font="Arial 18")

        ttk.Scrollbar(App.parent, orient=tk.HORIZONTAL).grid()
        ttk.Scrollbar(App.parent, orient=tk.VERTICAL).grid()
       
if __name__ == '__main__':
    Demo().run()