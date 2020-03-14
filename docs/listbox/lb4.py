# <ListboxSelect> callback function and current selection
import tkinter as tk

def cb(event):
    label['text'] = str(event) + '\n' + str(lb.curselection())

root = tk.Tk()
var = tk.StringVar(value=dir(tk))

label = tk.Label(root)
label.grid()

lb = tk.Listbox(root, listvariable=var, selectmode='extended')
lb.grid()
lb.bind('<<ListboxSelect>>', cb)

root.mainloop()