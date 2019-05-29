"""Add a status bar."""

import tkinter as tk
from tklib import *

def callback(event):
    print(event)

class Demo(App):
    def __init__(self):
        super(Demo, self).__init__()
        Label('Statusbar', font='Arial 24')
        Label('print Motion event to status bar')
        
        App.root.bind('<Motion>', self.cb)
        App.root.bind('<Key>', self.cb)

        Frame()
        Button()
        Label()
        Entry('Entry', 'App.status["text"]=self.val.get()')

    def cb(self, event):
        App.status['text'] = event

if __name__ == '__main__':
    Demo().run()