"""Tabbed Text widgets."""
from tklib import *

class Demo(App):
    def __init__(self, **kwargs):
        super(Demo, self).__init__(**kwargs)
        Label('Tabbed Text Widgets', font='Arial 24')
        Button('Add tab', 'Frame(nb="Tab")')
        
        Notebook()
        Frame(nb='Tab 1')
        Text()
        Frame(nb='Tab 2')
        Text()
        Frame(nb='Tab 3')
        Text()

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