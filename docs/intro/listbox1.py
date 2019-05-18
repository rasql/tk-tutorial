"""Place a listbox."""

import tkinter as tk
from tklib import *
import random

class Demo(App):
    def __init__(self): 
        super(Demo, self).__init__()
        Label("Listbox browse", font="Arial 18")
        Listbox('Mon;Tue;Wed;Thu;Fri;Sat;Sun', 'print(self)')

        Label("Listbox multiple", font="Arial 18")
        Listbox('Mon;Tue;Wed;Thu;Fri;Sat;Sun', selectmode=tk.MULTIPLE)

        Label("Listbox extended", font="Arial 18")
        Listbox('Mon;Tue;Wed;Thu;Fri;Sat;Sun', selectmode=tk.EXTENDED)

if __name__ == '__main__':
    Demo().run()