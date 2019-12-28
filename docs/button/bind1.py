import tkinter as tk

root = tk.Tk()
l = tk.Label(root, text='starting...', font='Arial 36')
l.pack()

l.bind('<Enter>', lambda e: l.configure(text='mouse inside'))
l.bind('<Leave>', lambda e: l.configure(text='mouse outside'))
l.bind('<1>', lambda e: l.configure(text='mouse click'))

root.mainloop()

