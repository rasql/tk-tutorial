"""Add a status bars to different windows."""

import tkinter as tk
from tklib import *

def callback(event):
    print(event)

class Demo(App):
    def __init__(self):
        super(Demo, self).__init__()
        Label('Statusbar for different windows', font='Arial 24')
        Label('print Motion event to status bar')
        
        App.root.bind('<Motion>', self.cb)
        App.root.bind('<Key>', self.cb)

        Window('Key event to status bar')
        Label('Show mouse motion in stauts bar', font='Arial 24')
        Frame()
        Button()
        Label()
        App.win.bind('<Motion>', self.cb)

    def cb(self, event):
        App.status['text'] = event

if __name__ == '__main__':
    Demo().run()