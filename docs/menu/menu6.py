"""Insert items at a specific index. 
This is possible using the Menu.insert() method."""
from tklib import *

class Demo(App):
    def __init__(self):
        super().__init__()
        Label("Insert items at specific index.", font="Arial 24")
   
        Menu('Menu')
        for i in range(5):
            Item('Item {}'.format(i), cmd=lambda : print(i), acc='Command-'+str(i))

        Item('Item', 'print("Left")', acc='Command-Left')
        Item('Item', 'print("Up")', acc='Command-Up')
        Item('Item', 'print("Right")', acc='Command-Right')
        Item('Item', 'print("Down")', acc='Command-Down')
        
        App.menus[-1].insert(2, 'command', label='Extra item')
        App.menus[-1].insert(100, 'command', label='Extra item 100')
        App.menus[-1].insert(10, 'command', label='Extra item 10')

        Menu('Window', name='window')
        Menu('Help', name='help')

Demo().run()