"""Tabbed Text widgets."""
from tklib import *

class Demo(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Label('Tabbed text widgets', font='Arial 24')
       
        Button('Add tab', 'Frame(nb="Tab");Text()')
        Notebook()
        Frame(nb='Tab 1')
        Text()
        Frame(nb='Tab 2')
        Text()

Demo().run()