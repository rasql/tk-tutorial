"""Use regex to search in a listbox."""
from tklib import *
import builtins
import math
import os
import re

class ListboxSearch():
    def __init__(self, items, **kwargs):
        Frame().grid(sticky='ns')
        self.re = Entry('regex', self.filter, width=15)
        self.lb = Listbox(items, **kwargs)
        self.lb.bind('<<ListboxSelect>>', self.cb)
        App.stack.pop()

    def filter(self, event=None):
        p = self.re.val.get()
        self.lb.delete(0, 'end')
        self.lb.filtered = []
        for s in self.lb.items:
            m = re.match(p, s)
            if m:
                self.lb.insert('end', s)
        self.lb.coloring()
    
    def cb(self, event):
        sel = self.lb.curselection()[0]
        self.item = self.lb.get(sel)
        s = 'math.'+self.item+'.__doc__'
        doc = eval(s)
        App.text.insert('end', self.item + '\n' + doc + '\n')

class Demo(App):
    def __init__(self): 
        super().__init__()
        Label("Listbox with search", font="Arial 18")

        App.obj = math
        App.obj_name = App.obj.__name__
        App.dir = dir(App.obj)

        ListboxSearch(App.dir, height=20)
        App.text = Text()
        App.text.grid(row=1, column=1)

Demo().run()