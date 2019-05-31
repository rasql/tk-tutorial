"""Automatic labels."""

from tklib import *

def cb(event=None):
    print('callback')

root = tk.Tk()

Frame()
Combobox()
Entry()
Scale()
Spinbox()

Frame()
Combobox('Combobox', 'Mon;Tue;Wed', cb)
Combobox('Combobox', 'Mon;Tue;Wed', 'print(self.get())')

Entry('Entry', cb)
Entry('Entry', 'print(self.get())')

Scale('Scale', cb)
Scale('Scale', 'print(self.get())')
Scale('Scale', 'print(self.get())', orient='vertical')

Spinbox('Spinbox', cb)
Spinbox('Spinbox', 'print(self.get())')

root.mainloop()