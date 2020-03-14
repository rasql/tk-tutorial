# Create a listbox the old way, with the insert/delete method
import tkinter as tk

root = tk.Tk()

lb = tk.Listbox(root)
lb.grid()

lb.insert(0, 'item0', 'item1', 'item2')
lb.delete(1)

items = dir(tk)
for item in items:
    lb.insert(tk.END, item)
lb.insert(tk.END, *items)

root.mainloop()