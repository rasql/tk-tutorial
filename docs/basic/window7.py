"""Tabbed notebook windows."""
import tkinter as tk
import tkinter.ttk as ttk
from tklib import *

class Demo(App):
    def __init__(self, **kwargs):
        super(Demo, self).__init__(**kwargs)
        App.root.title('Windows')

        Label('Tabbed Notbooks', font='Arial 24')
        Notebook()
        Frame(nb='Frame One')
        Frame(nb='Frame Two')

if __name__ == '__main__':
    Demo().run()