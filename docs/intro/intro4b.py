import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()

frame = ttk.Frame(root)
ttk.Label(frame, text='Label').grid()
ttk.Button(frame, text='Button', underline=0).grid()
ttk.Checkbutton(frame, text='Checkbutton', underline=1).grid()
ttk.Radiobutton(frame, text='Radiobutton').grid()
ttk.Entry(frame).grid()
ttk.Combobox(frame).grid()
ttk.Entry(frame).grid()
frame.grid()

tk.Listbox(root).grid(column=1, row=0)
tk.Text(root, width=20, height=10).grid(column=2, row=0)
tk.Canvas(root, width=200).grid(column=3, row=0)
        
root.mainloop()