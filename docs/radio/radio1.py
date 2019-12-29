import tkinter as tk
root = tk.Tk()

var = tk.StringVar()
var.set('English')

def cb():
    print(var.get())

tk.Radiobutton(root, text='English', variable=var, value='English', command=cb).pack()
tk.Radiobutton(root, text='German', variable=var, value='German', command=cb).pack()
tk.Radiobutton(root, text='French', variable=var, value='French', command=cb).pack()

root.mainloop()