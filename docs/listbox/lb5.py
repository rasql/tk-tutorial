# Edit listbox item with an entry widget
import tkinter as tk

def select(event):
    i = lb.curselection()[0]
    item.set(items[i])

def update(event):
    i = lb.curselection()[0]
    items[i] = item.get()
    var.set(items)

root = tk.Tk()
items = dir(tk)
var = tk.StringVar(value=items)

lb = tk.Listbox(root, listvariable=var)
lb.grid()
lb.bind('<<ListboxSelect>>', select)

item = tk.StringVar()
entry = tk.Entry(root, textvariable=item, width=20)
entry.grid()
entry.bind('<Return>', update)

root.mainloop()