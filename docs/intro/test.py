from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Example")
frame = Frame(root)
frame.grid()

nb = ttk.Notebook(frame)
nb.grid()
fr1 = ttk.Frame(nb)
nb.add(fr1, text="Frame One")
fr2 = ttk.Frame(nb)
nb.add(fr2, text="Frame Two")
print(nb, fr1)
print(nb, fr2)


#(The labels are examples, but the rest of the code is identical in structure). 

# labelA = ttk.Label(frame1, text = "This is on Frame One")
# labelA.grid(column=1, row=1)

# labelB = ttk.Label(frame2, text = "This is on Frame Two")
# labelB.grid(column=1, row=1)

root.mainloop()