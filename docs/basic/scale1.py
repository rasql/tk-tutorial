import tkinter as tk
import tkinter.ttk as ttk
from tklib import *

class Demo(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Label('Scale widget', font='Arial 24')
        
        Scale()
        Scale()
        Scale()

if __name__ == '__main__':
    Demo().run()