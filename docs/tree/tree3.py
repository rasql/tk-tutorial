"""Display a file Browser."""

import os
import tkinter as tk
from tklib import *

class Demo(App):
    def __init__(self): 
        super(Demo, self).__init__()
        Label('File browser', font='Arial 24')

        Label('OS name: ' + os.name)
        
        version = '\n'.join(list(os.uname()))
        
        cwd = os.getcwd()
        Label('Directory: ' + cwd)
      
        dir = os.listdir()
        tree = Treeview()
        for item in dir:
            size = os.stat(item).st_size
            tree.insert('', 'end', text=item, values=(size))

        tree['columns'] = ('size', 'value')
        tree.column('size', width=100, anchor='e')
        tree.heading('size', text='Size')
        tree.heading('value', text='Value')

if __name__ == '__main__':
    Demo().run()