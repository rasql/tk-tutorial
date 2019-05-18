"""Simple calculator."""

import tkinter as tk
import tkinter.ttk as ttk
from tklib import *

class Demo(App):
    def __init__(self, **kwargs):
        super(Demo, self).__init__(**kwargs)
        App.root.title('Calculator')

        frame = ttk.Frame(App.root)
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)
        
        cmd = 'print(self["text"])'

        Button('7', 'print(self)', padding=10).grid(sticky='nesw', padx=10, pady=10)
        Button('8', 'print(self.cmd)', padding=10).grid(column=1, row=0)
        Button('9', 'print(self.configure())', padding=10).grid(column=2, row=0)
        
        Button('4', cmd, padding=10).grid(row=1)
        Button('5', cmd, padding=10).grid(row=1, column=1)
        Button('6', cmd, padding=10).grid(row=1, column=2)
        
        Button('1', cmd, padding=10)
        Button('2', cmd, padding=10).grid(row=2, column=1)
        b = Button('3', 'print(123)', padding=10)
        b.grid(row=2, column=2)
        Label('Label')
        print(b)
        print(b.grid_info())

    def cb(self, x):
        print(self.widgetName, x)
        

if __name__ == '__main__':
    Demo().run()