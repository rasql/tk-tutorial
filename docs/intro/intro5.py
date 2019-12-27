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
    
if __name__ == '__main__':
    Demo().run()