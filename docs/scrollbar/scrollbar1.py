"""Display scrollbars."""
from tklib import *

class Demo(App):
    def __init__(self): 
        super().__init__()
        Label("Scrollbars", font="Arial 18")

        ttk.Scrollbar(App.stack[-1], orient=tk.HORIZONTAL).grid()
        ttk.Scrollbar(App.stack[-1], orient=tk.VERTICAL).grid()
       
Demo().run()