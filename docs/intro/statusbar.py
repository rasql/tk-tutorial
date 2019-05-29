"""Add a status bar."""

import tkinter as tk
from tklib import *

def callback(event):
    print(event)

class Demo(App):
    def __init__(self):
        super(Demo, self).__init__()
        Label('Statusbar', font='Arial 24')

        Frame()
        Button()
        Label()
        Entry('Entry', 'App.status["text"]=self.val.get()')

if __name__ == '__main__':
    Demo().run()