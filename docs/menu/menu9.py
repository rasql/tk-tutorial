"""Insert a popup menu."""
from tklib import *

class Demo(App):
    def __init__(self):
        super().__init__()
        Label("Insert widgets via the menu.", font="Arial 24")

        text = Text('Initial text...')
        
        ContextMenu(text)
        Item('Item 1', 'print(1)')
        Item('Item 2', 'print(2)')
        Item('Item 3', 'print(3)')

if __name__ == '__main__':
    Demo().run()