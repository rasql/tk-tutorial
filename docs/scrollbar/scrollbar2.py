"""Listbox with a scrollbar."""
from tklib import *

class Demo(App):
    def __init__(self): 
        super().__init__()
        Label("Listbox with scrollbars", font="Arial 18")

        lb = Listbox(list(range(100)))
        sb = ttk.Scrollbar(App.stack[-1])
        sb.grid(row=1, column=1, sticky='ns')

        lb.config(yscrollcommand=sb.set)
        sb.config(command=lb.yview)

Demo().run()