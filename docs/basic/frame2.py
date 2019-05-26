"""Speparate frames."""
from tklib import *

class Demo(App):
    def __init__(self, **kwargs):
        super(Demo, self).__init__(**kwargs)

        Label('Embedded frames', font='Arial 24')

        Frame()
        Button()
        Entry()
        
        Frame()
        Button()
        Entry()

        App.stack.pop()
        App.stack.pop()
        Button()
        Frame()
        Button()
        Entry()
        
       

if __name__ == '__main__':
    Demo().run()