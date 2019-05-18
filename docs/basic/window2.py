"""Standard dialogs."""

import tkinter as tk
import tkinter.ttk as ttk
from tklib import *
from tkinter import filedialog

class Demo(App):
    def __init__(self, **kwargs):
        super(Demo, self).__init__(**kwargs)
        App.root.title('Windows and dialogs')
        Label('Standard Dialogs', font='Arial 24')

        Button('Open…', 'App.open["text"] = tk.filedialog.askopenfilename()')
        App.open = Label('File')

        Button('Save…', 'App.save["text"] = tk.filedialog.asksaveasfilename()')
        App.save = Label('File')

        Button('Directory', 'App.dir["text"] = tk.filedialog.askdirectory()')
        App.dir = Label('Directory')

if __name__ == '__main__':
    Demo().run()