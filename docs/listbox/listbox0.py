import tkinter as tk

def cb(e):
    print(e, lb.curselection())

root = tk.Tk()

attributes = dir(tk)
var = tk.StringVar(value=dir(tk))

lb = tk.Listbox(root, listvariable=var, height=10)
lb.pack(side='left')

tk.Listbox(root, listvariable=var, selectmode='extended').pack(side='left')
tk.Listbox(root, listvariable=var, selectmode='none').pack(side='left')

lb.bind('<<ListboxSelect>>', cb)
lb.bind('<Double-1>', cb)
root.bind('<Return>', cb)

root.mainloop()