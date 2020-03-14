"""Canvas configuration with Treeview"""
from tklib import *

class Option:
    def __init__(self, widget):
        self.w = widget
        tree = Treeview(columns=(0))
        tree.column(0, width=150)
        tree.heading(0, text='Value')
        tree.grid(row=0, column=2)

        d = self.w.config()
        print(d)
        for (k, v) in d.items():
            if len(v)>2:
                tree.insert('', 'end', text=k, values=v[-1])


class Demo(App):
    def __init__(self): 
        super().__init__()
        Label("Canvas configuration", font="Arial 24")

        App.stack[-1]=Frame()
        App.c = Canvas(background='lightblue',
            borderwidth=10,
            height=250)
        d = App.c.config()

        tree = Treeview(columns=(0))
        tree.column(0, width=150)
        tree.heading(0, text='Value')
        tree.grid(row=0, column=1)

        for (k, v) in d.items():
            if len(v)>2:
                tree.insert('', 'end', text=k, values=v[-1])

        Option(App.c)

Demo().run()