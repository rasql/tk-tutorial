import tkinter as tk

root = tk.Tk()

var0 = tk.StringVar()
var1 = tk.StringVar()
var2 = tk.StringVar()

var0.set('1')
var1.set('0')
var2.set('0')

def cb():
    print('--- languages ---')
    print('English', var0.get())
    print('German', var1.get())
    print('French', var2.get())

tk.Checkbutton(root, text='English', variable=var0, command=cb).pack()
tk.Checkbutton(root, text='German', variable=var1, offvalue='barely', command=cb).pack()
tk.Checkbutton(root, text='French', variable=var2, onvalue='fluent' command=cb).pack()

root.mainloop()