# Show browse/extended selectmode
import tkinter as tk

root = tk.Tk()

var = tk.StringVar(value=dir(tk))

tk.Listbox(root, listvariable=var, selectmode='browse').pack(side='left')
tk.Listbox(root, listvariable=var, selectmode='extended').pack(side='left')

root.mainloop()
root.mainloop()