import tkinter as tk
root = tk.Tk()

name = tk.StringVar()
tk.Label(text='Name').pack()
tk.Entry(root, textvariable=name, width=10).pack()

password = tk.StringVar()
tk.Label(text='Password').pack()
tk.Entry(root, textvariable=password, show='*').pack()

root.mainloop()