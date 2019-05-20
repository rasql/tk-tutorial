"""Scrolling a Text."""

from tklib import *

class Demo(App):
    def __init__(self): 
        super(Demo, self).__init__()
        Label('Scrollable text', font='Arial 24')

        text = 'long ' * 20
        text += 'line\n' * 20

        Label("No scrollbars")
        Text(text, height=5, wrap='none')

        Label("X scrollbars")
        Text(text, height=5, scroll='x', wrap='none')

        Label("Y scrollbars")
        Text(text, height=5, scroll='y', wrap='none')

        Label("XY scrollbars")
        Text(text, height=5, scroll='xy', wrap='none')

if __name__ == '__main__':
    Demo().run()