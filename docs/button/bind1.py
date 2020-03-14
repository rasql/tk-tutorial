import tkinter as tk

root = tk.Tk()
label = tk.Label(root, text='starting...', font='Arial 36')
label.pack()

label.bind('<Enter>', lambda e: l.configure(text='mouse inside'))
label.bind('<Leave>', lambda e: l.configure(text='mouse outside'))
label.bind('<1>', lambda e: l.configure(text='mouse click'))

root.mainloop()