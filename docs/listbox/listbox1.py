"""Place a listbox."""

import tkinter as tk
from tklib import *
import os

class Demo(App):
    def __init__(self): 
        super(Demo, self).__init__()
        Label("Listbox browse", font="Arial 18")

        App.i = Spinbox('index')
        Entry('value', 'App.lb.insert(App.i.val.get(), self.get())')
        Button('Insert')

        L = dir(os)
        print(len(L))

        print(len(L), L)
        App.lb = Listbox(L)
        App.lb.grid()

        Button('coloring()', 'App.lb.coloring()')
        Button('delete()', 'App.lb.delete(0, "end")')

        # App.var.set(list(range(10)))
        Button('Set', 'App.var.set(list(range(100)))')
    
if __name__ == '__main__':
    Demo().run()