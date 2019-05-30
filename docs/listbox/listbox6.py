"""Use regex to search in a listbox."""

from tklib import *
import tkinter as tk

def set(event=None):
    App.lb.obj = App.en.val.get()
    L = dir(eval(App.lb.obj))
    App.lb.set(L)
    App.lb.coloring()

class Demo(App):
    def __init__(self): 
        super(Demo, self).__init__()
        Label("Listbox with search", font="Arial 18")
        App.en = Entry('object', set)

        App.obj = tk
        App.obj_name = App.obj.__name__
        App.dir = dir(App.obj)

        App.lb = ListboxSearch(App.dir, height=20, )
        App.text = Text()
        App.text.grid(row=2, column=1)


if __name__ == '__main__':
    Demo().run()