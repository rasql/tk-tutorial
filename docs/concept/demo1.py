import tkinter as tk
from tklib import *



class Demo(App):
    def __init__(self, **kwargs):
        super(Demo, self).__init__(**kwargs)
        App.root.title = 'Feet to meters'
        Label('feet')
        Label('is equivalent to')
        Label('meters')
        
if __name__ == '__main__':
    Demo().run()