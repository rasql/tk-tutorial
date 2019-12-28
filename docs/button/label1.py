import tkinter as tk

root = tk.Tk()
str = tk.StringVar()
str.set('dynamic text')

tk.Label(root, text='static text').pack()
tk.Label(root, textvariable=str).pack()
tk.Label(root, text='both', textvariable=str).pack()
tk.Label(root, text='Arial 24', font='Arial 24').pack()
tk.Label(root, text='foreground=red', foreground='red').pack()

root.mainloop()