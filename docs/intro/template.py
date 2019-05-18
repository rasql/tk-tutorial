"""Base your program on this template."""

import tkinter as tk
from tklib import *

def callback(event):
    print(event)

class Demo(App):
    def __init__(self):
        super(Demo, self).__init__()
        Label('Template')

        self.var = tk.IntVar()
        ch = tk.ttk.Checkbutton(App.parent, text='checkbox', variable=self.var, command=callback, takefocus=0)
        self.var.set(1)
        ch.pack()
        print(self.var.get(), ch['onvalue'], ch['offvalue'])

        self.var2 = tk.IntVar()
        c = tk.Checkbutton(App.parent, text="Expand", variable=self.var2)
        c.pack()
    
        self.var3 = tk.IntVar()
        self.var3.set(1)
        c = tk.ttk.Checkbutton(App.parent, text="Expand", variable=self.var3)
        c.pack()

if __name__ == '__main__':
    Demo().run()