from tklib import *
app = App('insert and delete')

def insert():
    i = int(index.var.get())
    listbox.insert(i, value.var.get())

def delete():
    i = int(index.var.get())
    listbox.delete(i)

index = Entry('index', 'print(self.var.get())', val=0)
value = Entry('value', 'print(self.var.get())', val='new item')

Button('Insert', insert)
Button('Delete', delete)

listbox = tk.Listbox(App.stack[-1], height=10)
listbox.grid()

app.run()