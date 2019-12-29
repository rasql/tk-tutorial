"""Menus with items, separators, checkboxes and radiobuttons."""
from tklib import *

class Demo(App):
    def __init__(self):
        super().__init__()
        Label("Checkbuttones and radiobuttons.", font="Arial 24")

        Menu('Checkbutton')
        for i in range(5):
            Item('*Item {}'.format(i))

        Menu('Radiobutton')
        radio = tk.StringVar()
        for i in range(5):
            Item('#Item {}'.format(i), variable=radio)

        Menu('Help', name='help')

Demo().run()