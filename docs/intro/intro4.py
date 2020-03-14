# setting options
import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
ttk.Button(root, text='Set options at creation').grid()

button = ttk.Button(root)
button['text'] = 'Set options as dict'
button.grid()

button = ttk.Button(root)
button.config(text='Set options with config() method')
button.grid()

options = button.config()
for x in options:
    print(x, options[x])

print(button.keys())

root.mainloop()