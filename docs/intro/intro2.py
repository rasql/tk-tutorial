import tkinter as tk
from tklib import *

class Intro(App):
    def __init__(self):
        super(Intro, self).__init__()
        self.logo = tk.PhotoImage(file='python_logo.png')

        self.w1 = tk.Label(self.root, image=self.logo).pack(side='right')

        explanation = """At present, only GIF and PPM/PGM
        formats are supported, but an interface 
        exists to allow additional image file
        formats to be added easily."""

        self.w2 = tk.Label(self.root, 
                    justify=tk.LEFT,
                    padx = 10, 
                    text=explanation).pack(side='left')

if __name__ == '__main__':
    Intro().run()