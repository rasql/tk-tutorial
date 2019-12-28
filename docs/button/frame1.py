import tkinter as tk

root = tk.Tk()

for x in ('flat', 'raised', 'sunken', 'solid', 'ridge', 'groove'):
    frame = tk.Frame(root, relief=x, borderwidth=5)
    frame.pack(side='left')
    tk.Label(frame, text=x).pack()

root.mainloop()