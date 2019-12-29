"""Create a combobox."""
import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()

day = tk.StringVar()
day.set('Wednesday')
days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')

tk.Label(text='combobox with text entry').pack()
combo = ttk.Combobox(root, textvariable=day, values=days)
combo.pack()

day2 = tk.StringVar()
day2.set('Friday')
tk.Label(text='state=readonly').pack()
ttk.Combobox(root, textvariable=day2, values=days, state='readonly').pack()

root.mainloop()