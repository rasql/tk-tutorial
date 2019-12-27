"""Widget browser."""

import os
import tkinter as tk
from tklib import *

def DemoWin():
    Window()
    Frame()
    Button()
    Button()
    Label()

    Frame()
    Entry('search')
    Scale()
    Canvas()

class WidgetBrowser():
    def __init__(self, widget):
        self.tree = Treeview()
        root = widget.winfo_toplevel()
        self.add_node(w=root)
        self.tree['columns'] = range(3)
        # self.tree.column(0, width=100, anchor='e')
        # self.tree.heading('size', text='Size')

    def add_node(self, w, id=''):
        """Add widget tree."""
        print(w)
        g = w.winfo_geometry()
        c = w.winfo_class()
        id = self.tree.insert(id, 'end', text=w, values=(g, c))
        for w in w.winfo_children():
            self.add_node(w, id)

class Demo(App):
    def __init__(self): 
        super().__init__()
        Label('Widget browser', font='Arial 24')
        b = Button('New Window', DemoWin)
    
        WidgetBrowser(b)
        
if __name__ == '__main__':
    Demo().run()