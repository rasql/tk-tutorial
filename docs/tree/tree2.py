"""Display tk Text."""

import tkinter as tk
from tklib import *

class Demo(App):
    def __init__(self): 
        super(Demo, self).__init__()
        Label('Treeview', font='Arial 24')

        items = dir(tk)
        tree = Treeview()
        tree['columns'] = ('type', 'value')
        tree.column('type', width=100)
        tree.heading('type', text='Type')
        tree.heading('value', text='Value')

        for item in items:
            x = eval('tk.'+item)
            t = type(x)
            print(t.__name__, x)
            tree.insert('', 'end', text=item, values=(t.__name__, x))

        items = dir()
        Treeview(items).grid(row=1, column=1)

if __name__ == '__main__':
    Demo().run()