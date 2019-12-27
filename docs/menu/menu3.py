"""Add menus, items and sub-menus."""
from tklib import *

class Demo(App):
    def __init__(self):
        super().__init__()
        Label("Menu bar with sub-menus", font="Arial 24")

        for i in range(1, 7):
            Menu('Menu ' + str(i))
            for c in "ABCDEF":
                label = 'Item {}{}'.format(i, c)
                cmd = 'print("{}")'.format(label)
                Item(label, cmd, 'Command-{}'.format(c.lower()))

        for i in range(1, 7):
            Menu('Submenu in {}'.format(i), i)
            for c in 'XYZ':
                Item('Item ' + c, 'print(123)', 'Control-' + c.lower())
            Item('Add Item to {}'.format(i), id=i)

Demo().run()