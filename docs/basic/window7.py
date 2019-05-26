"""Tabbed notebooks."""
from tklib import *

class Demo(App):
    def __init__(self, **kwargs):
        super(Demo, self).__init__(**kwargs)
        Label('Tabbed Notebooks', font='Arial 24')
        Button()
        
        Notebook()
        Frame(nb='Tab 1')
        Button()
        Frame(nb='Tab 2')
        Entry()
        Frame(nb='Tab 3')
        Canvas(height=100)

        Notebook()
        Frame(nb='Tab 1')
        Button()
        Button()
        Frame(nb='Tab 2')
        Entry()
        Frame(nb='Tab 3')
        Canvas(height=100)

if __name__ == '__main__':
    Demo().run()