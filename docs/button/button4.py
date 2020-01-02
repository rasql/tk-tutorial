import tkinter as tk
root = tk.Tk()

tk.Button(text='Button 123', command=lambda : exec('print(123)')).pack()
tk.Button(text='Button 456', command=lambda : exec('print(456)')).pack()
tk.Button(text='Button 789', command=lambda : exec('print(789)')).pack()

root.mainloop()