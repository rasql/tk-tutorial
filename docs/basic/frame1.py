"""Embedded frames."""
from tklib import *

class Demo(App):
    def __init__(self):
        super().__init__()
        Label('Embedded frames', font='Arial 24')

        types = ['flat', 'raised', 'sunken', 'solid', 'ridge', 'groove']
        for t in types:
            Frame(relief=t, padding=(50, 5), borderwidth=5)
            Label(t)

Demo().run()