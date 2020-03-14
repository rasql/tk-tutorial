# Display a simple listbox
import tkinter as tk

root = tk.Tk()

items = dir(tk)
var = tk.StringVar()
var.set(items)
tk.Listbox(root, listvariable=var).grid()

root.mainloop()