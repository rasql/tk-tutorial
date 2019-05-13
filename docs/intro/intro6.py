"""Create radio buttons."""

import tkinter as tk
from tklib import *

class Intro(App):
    def __init__(self):
        super(Intro, self).__init__()
        Lb("Checkbox demo", fg="red", font="Arial 24")
        Rb('Python;Perl;Ruby;Java;C++')
        Lb('Day of the week', fg='blue')
        Rb('Mon;Tue;Wed;Thu;Fri', command='print("day")')
    
if __name__ == '__main__':
    Intro().run()