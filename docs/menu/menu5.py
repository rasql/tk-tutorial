"""Create a context menu."""
from tklib import *

class Demo(App):
    def __init__(self):
        super().__init__()
        l1 = Label("Context Menu", font="Arial 24")
        l2 = Label("Context Menu 2", font="Arial 48")
        
        ContextMenu(l1)
        Item('Item 1', 'print(1)')
        Item('Item 2', 'print(2)')
        Item('Item 3', 'print(3)')
        
        ContextMenu(l2)
        for c in 'ABC':
            Item('Item ' + c)

        ContextMenu(App.root)
        Item('Cut', 'print("Cut")')
        Item('Copy', 'print("Copy")')

Demo().run()