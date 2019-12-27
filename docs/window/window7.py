"""Tabbed notebooks."""
from tklib import *

class Demo(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Label('Tabbed Notebooks', font='Arial 24')
        Button()
        
        Notebook()
        Frame(nb='Tab 1')
        Button()
        Frame(nb='Tab 2')
        Entry()
        Frame(nb='Tab 3')
        Canvas(height=100)
        App.stack.pop()

        Notebook()
        Frame(nb='Tab 1')
        Button()
        Button()
        Frame(nb='Tab 2')
        Entry()
        Frame(nb='Tab 3')
        Canvas(height=100)

Demo().run()