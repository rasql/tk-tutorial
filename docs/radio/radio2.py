import tkinter as tk
root = tk.Tk()

items = ('English', 'German', 'French')
var = tk.StringVar()
var.set(items[0])

def cb():
    print(var.get())

for x in items:
    tk.Radiobutton(root, text=x, variable=var, value=x, command=cb).pack()

root.mainloop()