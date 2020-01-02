"""Create entry fields."""
from tklib import *
app = App('Entry')

Label('Entry fields', font='Arial 24')
Entry('First name:', 'print(self.var.get())', 'James')
Entry('Last name:', 'print(self.var.get())')
Entry('Password:', 'print(self.var.get())', show='*')

Entry('Enter expression', 'App.res["text"] = eval(self.var.get())')
App.res = Label('Result')

app.run()
