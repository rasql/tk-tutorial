"""Canvas configuration with Treeview"""
from tklib import *

class Demo(App):
    def __init__(self): 
        super(Demo, self).__init__()
        Label("Canvas configuration", font="Arial 24")

        App.parent=Frame()
        App.c = Canvas()
        d = App.c.config()

        tree = Treeview(columns=(0))
        tree.column(0, width=150)
        tree.heading(0, text='Value')
        tree.grid(row=0, column=1)

        for (k, v) in d.items():
            if len(v)>2:
                tree.insert('', 'end', text=k, values=v[-1])

if __name__ == '__main__':
    Demo().run()