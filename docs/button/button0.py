import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
"""Advantages
- same class name (Button)
- automatic parent (previous)
- keyword not needed (text, command)
- default text (Button)
- command string (instead of function)
- bind to Return key
- automatic placement (grid)
"""

class Button(ttk.Button):
    def __init__(self, text='Button', cmd='', **kwargs):
        self.cmd = cmd
        super().__init__(root, text=text, command=self.cb, **kwargs)
        self.bind('<Return>', self.cb)
        self.grid()
    
    def cb(self, event=None):
        if isinstance(self.cmd, str):
            exec(self.cmd)
        else:
            self.cmd()

def callback():
    print('callback function')

ttk.Button(root, text='ttk Button', command=callback).grid()
Button(cmd=callback)
Button('string', 'print("callback string")')
Button('func', callback)
Button('func', callback, pad=10)

root.mainloop()