"""Create entry fields."""
from tklib import *

class Demo(App):
    def __init__(self):
        super().__init__()
        Label('Entry fields', font='Arial 24')
        Entry('First name:', 'print(self.var.get())')
        Entry('Last name:', 'print(self.var.get())')
        Entry('Password:', 'print(self.var.get())', show='*')

        Entry('Enter expression', 'App.res["text"] = eval(self.var.get())')
        App.res = Label('Result')

Demo().run()