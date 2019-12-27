"""Add menus and items."""
from tklib import *

class Demo(App):
    def __init__(self):
        super().__init__()
        Label("Menu bar with items", font="Arial 24")

        for i in range(1, 7):
            Menu('Menu ' + str(i))
            for c in "ABCDEF":
                label = 'Item {}{}'.format(i, c)
                cmd = 'print("{}")'.format(label)
                Item(label, cmd, 'Command-{}'.format(c.lower()))

Demo().run()