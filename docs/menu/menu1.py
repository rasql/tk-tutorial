"""Add menus to the menubar."""
from tklib import *

class Demo(App):
    def __init__(self):
        super().__init__()
        Label("Menu bar without items", font="Arial 24")
        
        for i in range(1, 7):
            Menu('Menu ' + str(i))

Demo().run()