"""Selecting colors."""

import tkinter as tk
import tkinter.ttk as ttk
from tklib import *
from tkinter import filedialog
from tkinter import colorchooser

class Demo(App):
    def __init__(self, **kwargs):
        super(Demo, self).__init__(**kwargs)
        App.root.title('Windows and dialogs')
        Label('Color chooser', font='Arial 24')

        Button('Select color…', 'App.col["text"] = tk.colorchooser.askcolor()')
        App.col = Label('Color')

if __name__ == '__main__':
    Demo().run()