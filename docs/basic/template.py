"""Use this template to start an App."""

import tkinter as tk
import tkinter.ttk as ttk
from tklib import *

class Demo(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        App.root.title = 'Tk application template'
        Label('Demo application', font='Arial 24')

if __name__ == '__main__':
    Demo().run()