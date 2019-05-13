"""Create Labels with options. Set window title and maximum window size."""

import tkinter as tk
from tklib import *

class Intro(App):
    def __init__(self):
        super(Intro, self).__init__()
        Lb("Red Text in Times Font", fg="red", font="Times 24")
        Lb("Green Text in Helvetica Font", fg="light green", bg="dark green",
		 font="Helvetica 16 bold italic")
        Lb("Blue Text in Verdana bold", fg="blue", bg="yellow", font="Verdana 30 bold")
        
        App.root.title('My Application')
        App.root.maxsize(640,320)

if __name__ == '__main__':
    Intro().run()