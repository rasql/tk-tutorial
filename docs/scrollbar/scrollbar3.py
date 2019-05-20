"""Canvas with vertical and horizontal scrollbars."""

from tklib import *

class Demo(App):
    def __init__(self): 
        super(Demo, self).__init__()
        Label('Canvas with scrollbars', font='Arial 24')

        Label("No scrollbars")
        Canvas(height=100)

        Label("No scrollbars")
        Canvas(height=100, scroll='y')

if __name__ == '__main__':
    Demo().run()