"""React to events."""

import tkinter as tk
from tklib import *

def do_event(event):
    print('event', event) 


class Intro(App):
    def __init__(self):
        super(Intro, self).__init__()
        Label("React to events", fg="red", font="Arial 24")
        b = Button('Mouse clicks', 'print(123)')
        
        self.bind('<Button-1>', do_event)
        b.bind('<Double-1>', do_event)
        
    
if __name__ == '__main__':
    Intro().run()