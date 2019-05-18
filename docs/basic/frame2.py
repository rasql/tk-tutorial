"""Speparate frames."""
from tklib import *

class Demo(App):
    def __init__(self, **kwargs):
        super(Demo, self).__init__(**kwargs)

        Label('Separate frames', font='Arial 24')

        types = ['flat', 'raised', 'sunken', 'solid', 'ridge', 'groove']
        for t in types:
            Frame(relief=t, padding=(50, 5), borderwidth=5)
            Label(t)
            App.parent = App.stack.pop()

if __name__ == '__main__':
    Demo().run()