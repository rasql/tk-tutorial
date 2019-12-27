"""Insert different menus for each window."""
from tklib import *

def Menu1():
    Menu('Letters')
    for c in 'ABC':
        Item('Item ' + c) 

def Menu2():
    Menu('Numbers')
    for c in '123':
        Item('Item ' + c) 

class Demo(App):
    # constructor
    def __init__(self):
        super().__init__()
        Label("Different menus for each window.", font="Arial 24")

        Menu1()
        Menu2()

        Window("Letters")
        Button()
        Entry()
        Menu1()
        Menu('Help', name='help')

        Window("Numbers")
        Entry()
        Menu2()

Demo().run()