"""Listbox with a scrollbar."""

import tkinter.ttk as ttk
from tklib import *

class Demo(App):
    def __init__(self): 
        super(Demo, self).__init__()
        Label("Listbox with scrollbars", font="Arial 18")

        lb = Listbox(list(range(100)))
        sb = ttk.Scrollbar(App.stack[-1])
        sb.grid(row=1, column=1, sticky='ns')

        lb.config(yscrollcommand=sb.set)
        sb.config(command=lb.yview)

if __name__ == '__main__':
    Demo().run()