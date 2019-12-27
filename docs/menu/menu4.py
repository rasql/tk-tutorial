"""Menus with items, separators, checkboxes and radiobuttons."""
from tklib import *

class Demo(App):
    def __init__(self):
        super().__init__()
        Label("Checkboxes and radiobuttons.", font="Arial 24")

        Menu('Checkbox')
        for i in range(5):
            Item('*Item {}'.format(i))

        Menu('Radiobutton')
        radio = tk.StringVar()
        for i in range(5):
            Item('#Item {}'.format(i), variable=radio)

        Menu('Help', name='help')

Demo().run()