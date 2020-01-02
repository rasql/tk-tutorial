from tklib import *
import os

app = App('Listbox with insert')

def insert():
    i = int(index.var.get())
    print(i)
    print(value.var.get())


Label("Listbox browse", font="Arial 18")

index = Spinbox('index', 5)
value = Entry('value', 'App.lb.insert(App.i.val.get(), self.get())')
Button('Insert', insert)

listbox = Listbox(dir(os))
listbox.grid()

Button('coloring()', 'App.lb.coloring()')
Button('delete()', 'App.lb.delete(0, "end")')

Button('Set', 'App.var.set(list(range(100)))')
    
app.run()