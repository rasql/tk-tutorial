"""Place a listbox."""

import tkinter as tk
from tklib import *
import random

class Demo(App):
    def __init__(self): 
        super(Demo, self).__init__()
        Lb("Listbox browse", fg="red", font="Arial 18")
        Lbox('Mon;Tue;Wed;Thu;Fri;Sat;Sun')

        Lb("Listbox multiple", fg="red", font="Arial 18")
        Lbox('Mon;Tue;Wed;Thu;Fri;Sat;Sun', selectmode=tk.MULTIPLE)

        Lb("Listbox extended", fg="red", font="Arial 18")
        Lbox('Mon;Tue;Wed;Thu;Fri;Sat;Sun', selectmode=tk.EXTENDED)

        self.save_img()

if __name__ == '__main__':
    Demo().run()