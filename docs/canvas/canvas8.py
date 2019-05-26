"""Draw lines."""
from tklib import *

class Demo(App):
    def __init__(self): 
        super(Demo, self).__init__()
        Label("Drawing lines", font="Arial 24")

        Spinbox('width', 'App.c["width"]=self.val.get()', inc=50, to=1000)
        Spinbox('height', 'App.c["height"]=self.val.get()', inc=50, to=1000)
        Combobox('fill', 'black;red;green;blue;orange;cyan', 
            'App.c.itemconfig(App.c.id, fill=self.val.get())')
        Spinbox('width', 'App.c.itemconfig(App.c.id, width=self.val.get())', from_=1, to=20)
        Button('Delete', 'App.c.delete(App.c.id)')
        Button('Delete All', 'App.c.delete("all")')
        
        App.c = Canvas()

if __name__ == '__main__':
    Demo().run()