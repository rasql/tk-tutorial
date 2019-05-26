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
        Combobox('type', 'arc;line;rectangle;oval', 
            'App.c.itemconfig(App.c.id, fill=self.val.get())')

        Button('Config', 'print(App.c.itemconfig(1))')
        
        App.c = Canvas()
        print(vars(App.c))
        print()
        print(dir(App.c))

        App.c.create_rectangle(20, 20, 150, 100)
    
if __name__ == '__main__':
    Demo().run()