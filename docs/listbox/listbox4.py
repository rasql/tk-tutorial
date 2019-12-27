"""Use regex to search in a listbox."""
from tklib import *
import re

class ListboxSearch():
    def __init__(self, items):
        Frame()
        self.re = Entry('regex', self.filter, width=15)
        self.lb = Listbox(items)
        App.stack.pop()

    def filter(self, event=None):
        p = self.re.val.get()
        self.lb.delete(0, 'end')
        for s in self.lb.items:
            m = re.match(p, s)
            if m:
                self.lb.insert('end', s)
        self.lb.coloring()

class Demo(App):
    def __init__(self): 
        super().__init__()
        Label("Listbox with search", font="Arial 18")

        App.obj = os
        App.obj_name = App.obj.__name__
        App.dir = dir(App.obj)

        ListboxSearch(App.dir)

Demo().run()