"""Comparing tk, ttk and tklib buttons."""

from tklib import *
print(dir())

root = tk.Tk()

tk.Button(root, text='tk.Button').grid()
ttk.Button(root, text='ttk.Button').grid()
Button()

root.mainloop()