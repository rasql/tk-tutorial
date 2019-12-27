"""Add Labelframes."""
from tklib import *

class Demo(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Label('Labelframe widget', font='Arial 24')

        Labelframe(text='Frame 1', padding=5)
        Button()
        Canvas(height=100)

        App.stack.pop()

        Labelframe(text='Frame 2', padding=5)
        Button()
        Entry()

        Frame()
        Button()
        Entry()
            
Demo().run()