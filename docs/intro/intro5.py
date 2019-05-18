"""Create buttons."""

from tklib import *

class Demo(App):
    def __init__(self):
        super(Demo, self).__init__()
        Label('Button demo',  font='Arial 24')
        Button('Start', 'print("Start")')
        Button('Stop', 'print("Stop")')
        Button('Self', 'print(self)')
        Button('Destroy', 'self.destroy()')
        Button('root', 'print(App.root)')
        Button('parent', 'print(App.parent)')
        Button('geometry', 'print(App.root.geometry())')
    
if __name__ == '__main__':
    Demo().run()