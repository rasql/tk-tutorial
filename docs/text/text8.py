"""Help browser."""

from tklib import *
import datetime

class Demo(App):
    def __init__(self): 
        super(Demo, self).__init__()
        Label("Help display", font="Arial 24")

        str = datetime.__doc__

        App.text = Text(str)
             
if __name__ == '__main__':
    Demo().run()