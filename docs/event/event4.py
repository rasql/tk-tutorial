# keyboard bindings
import tkinter as tk

def cb(event):
    text.insert('end', str(event) + '\n')

root = tk.Tk()
text = tk.Text(root)
text.grid()

root.bind('<Key>', cb)
root.bind('a', lambda e: cb('a'))
root.bind('A', lambda e: cb('A'))
root.bind('<Return>', lambda e: cb('Return'))
root.bind('<Escape>', lambda e: cb('Escape'))
root.bind('<Tab>', lambda e: cb('Tab'))
root.bind('<space>', lambda e: cb('space'))
root.bind('<F1>', lambda e: cb('F1'))

# modifier keys (left and right)
root.bind('<Shift_L>', lambda e: cb('Shift'))
root.bind('<Control_L>', lambda e: cb('Ctrl'))
root.bind('<Alt_L>', lambda e: cb('Alt'))
root.bind('<Meta_L>', lambda e: cb('Cmd'))
root.bind('<Super_L>', lambda e: cb('Fn'))

# modifier keys for arrows
root.bind('<Right>', lambda e: cb('Right'))
root.bind('<Shift-Right>', lambda e: cb('Shift-Right'))
root.bind('<Command-Right>', lambda e: cb('Command-Right'))

# clear screen
root.bind('<BackSpace>', lambda e: text.delete('1.0', 'end'))
root.mainloop()