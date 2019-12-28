import tkinter as tk
root = tk.Tk()

def callback(x):
    print('button', x)

tk.Button(text='Button 1', command=lambda : callback(1)).pack()
tk.Button(text='Button 2', command=lambda : callback(2)).pack()
tk.Button(text='Button 3', command=lambda : callback(3)).pack()

root.mainloop()