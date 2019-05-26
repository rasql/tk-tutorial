"""Canvas config."""
from tklib import *

class Demo(App):
    def __init__(self): 
        super(Demo, self).__init__()
        Label("Canvas configuration", font="Arial 24")

        Spinbox('width', 'App.c["width"]=self.val.get()', inc=50, to=1000)
        Spinbox('height', 'App.c["height"]=self.val.get()', inc=50, to=1000)
        Combobox('background', 'white;yellow;pink;light blue', 'App.c.config(background=self.val.get())')
        Combobox('highlightcolor', 'black;red;blue;green', 'App.c.config(highlightcolor=self.val.get())')
        Combobox('relief', 'flat;sunken;raised;groove', 'App.c.config(relief=self.val.get())')
        Combobox('state', 'normal;disabled;hidden', 'App.c.config(state=self.val.get())')
        Spinbox('borderwidth', 'App.c.config(borderwidth=self.val.get())')
        
        Button('Config', 'print(App.c.config())')

        App.c = Canvas()

if __name__ == '__main__':
    Demo().run()