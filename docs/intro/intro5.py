"""Create buttons."""

import tkinter as tk
from tklib import *

class Intro(App):
    def __init__(self):
        super(Intro, self).__init__()
        Lb("Button demo", fg="red", font="Arial 24")
        Bt('Start', 'print("Start")', fg='red')
        Bt('Stop', 'print("Stop")', fg='blue')
        Bt('Quit', quit)
        Bt('Self', 'print(self)')
    
if __name__ == '__main__':
    Intro().run()