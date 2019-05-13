"""Create entry fields."""

import tkinter as tk
from tklib import *

def evaluate(event):
    print(event)

class Intro(App):
    def __init__(self):
        super(Intro, self).__init__()
        Lb("Entry fields", fg="red", font="Arial 24")
        En('First name:')
        En('Last name:')
        En('Address:')
        exp = En("Enter expression:", fg="blue", font="Arial 18")

        self.entry = tk.Entry(App.root)
        self.entry.bind('<Return>', self.evaluate)
        self.entry.pack()
        self.res = tk.Label(text='Result')
        self.res.pack()

    def evaluate(self, event):
        exp = self.entry.get()
        print(exp)
        print(eval(exp))
        self.res.configure(text='Result: ' + str(eval(exp)))

if __name__ == '__main__':
    Intro().run()