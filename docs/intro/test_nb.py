from tkinter import *
import tkinter.ttk as ttk

root = Tk()

n = ttk.Notebook(root)
n.grid()
f1 = ttk.Frame(n)   # first page, which would get widgets gridded into it
f2 = ttk.Frame(n)   # second page
f1.grid()
f2.grid()
n.add(f1, text='One')
n.add(f2, text='Two')

root.mainloop()