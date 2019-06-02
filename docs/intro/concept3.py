"""Entry widgets with labels, default value and callback ."""

from tklib import *

def cb(event=None):
    print('callback')

root = tk.Tk()

Frame()
Combobox('Combobox', 'Mon;Tue;Wed', cb)
Combobox('Combobox', 'Mon;Tue;Wed', 'print(self.get())', 'Wed')

Entry('Entry', cb)
Entry('Entry', 'print(self.get())', 'text')

Scale('Scale', cb)
Scale('Scale', 'print(self.get())', 0.5)

Spinbox('Spinbox', cb)
Spinbox('Spinbox', 'print(self.get())', 50)

root.mainloop()