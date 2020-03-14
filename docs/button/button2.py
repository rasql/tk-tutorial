import tkinter as tk

root = tk.Tk()
root.title("Feet to meters")

feet = tk.StringVar()
meters = tk.StringVar()

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(0.3048 * value)
    except ValueError:
        pass

tk.Entry(root, width=10, textvariable=feet).pack()
tk.Button(root, text='Convert feet to meters', command=calculate).pack()
tk.Label(root, textvariable=meters).pack()

root.bind('<Return>', calculate)
root.mainloop()