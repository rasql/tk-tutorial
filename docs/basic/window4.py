"""Separators."""
from tklib import *

class Demo(App):
    def __init__(self, **kwargs):
        super(Demo, self).__init__(**kwargs)
        Label('Add widgets and Separators', font='Arial 24')
        Separator()

        Button('New button', 'Button()')
        Button('New label', 'Label()')
        Button('New separator', 'Separator()')
        Separator()
            
if __name__ == '__main__':
    Demo().run()