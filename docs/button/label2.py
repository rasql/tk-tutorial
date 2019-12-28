import tkinter as tk

root = tk.Tk()

for x in ('flat', 'raised', 'sunken', 'solid', 'ridge', 'groove'):
    tk.Label(root, text=x, relief=x, borderwidth=5).pack(side='left')

root.mainloop()