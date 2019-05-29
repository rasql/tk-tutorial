"""Display built-in functions listbox."""

from tklib import *
import builtins
import math
import os

class Browser(Listbox):
    def cb(self, event):
        pass

class Demo(App):
    def __init__(self): 
        super(Demo, self).__init__()
        Label("Tk attributes", font="Arial 18")

        App.obj = os
        App.obj_name = App.obj.__name__
        App.dir = dir(App.obj)

        Listbox(App.dir, height=22, cmd='print(self.item); App.T.set(eval(App.obj_name + "." + self.item).__doc__)')
        App.T = Text()
        App.T.grid(row=1, column=1)
        
        App.en = Entry('object=', 'print(self.val.get())', width=12)

        Button('obj', 'print(App.obj.__name__)')
        Button('dir(obj)', 'print(App.dir)')
        Button('dir[0]', 'print(App.dir[0].__doc__)')

if __name__ == '__main__':
    Demo().run()