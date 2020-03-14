"""Canvas config."""
from tklib import *

class Demo(App):
    def __init__(self): 
        super().__init__()
        Label("Canvas configuration", font="Arial 24")

        Spinbox('width', 'App.c["width"]=self.var.get()', inc=50, to=1000)
        Spinbox('height', 'App.c["height"]=self.var.get()', inc=50, to=1000)
        Combobox('background', 'white;yellow;pink;light blue', 'App.c.config(background=self.var.get())')
        Combobox('highlightcolor', 'black;red;blue;green', 'App.c.config(highlightcolor=self.var.get())')
        Combobox('relief', 'flat;sunken;raised;groove', 'App.c.config(relief=self.var.get())')
        Combobox('state', 'normal;disabled;hidden', 'App.c.config(state=self.var.get())')
        Spinbox('borderwidth', 'App.c.config(borderwidth=self.var.get())')
        
        Button('Config', 'print(App.c.config())')

        App.c = Canvas()

Demo().run()