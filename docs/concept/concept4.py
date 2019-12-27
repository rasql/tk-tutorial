"""Vertical, diagonal and horizontal placement of widgets."""
from tklib import *

class Demo(App):
    def __init__(self): 
        super(Demo, self).__init__()

        for i in range(3):
            Button()

        f = Frame()
        for i in range(3):
            Button().grid(column=i)

        App.stack.pop()
        f2 = Frame()
        f2.grid(column=1)
        for i in range(3):
            Button().grid(column=i, row=0)

        print(f.grid_size())
        print(f2.grid_size())
        print(f.grid_slaves())
        print(f.grid_info())
        print(f2.grid_info())

        self.win.status['text'] = 'a\na'
    
if __name__ == '__main__':
    Demo().run()
