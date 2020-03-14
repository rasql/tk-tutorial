# draw straight lines on a canvas
from tklib import *

class Canvas(tk.Canvas):
    """Define a canvas with line drawing"""

    def __init__(self, **kwargs):
        # super(Canvas, self).__init__(App.stack[-1], width=w, height=h, bg='light blue')
        super(Canvas, self).__init__(App.stack[-1], **kwargs)
        self.grid()
        self.bind('<Button-1>', self.start)
        self.bind('<B1-Motion>', self.move)
        self.bind('<D>', self.print_msg)
        self.bind('<Key>', self.print_msg)
        self.bind('<Return>', self.print_msg)
        

    def start(self, event=None):
        # Execute a callback function.
        self.x0 = event.x
        self.y0 = event.y
        self.id = self.create_line(self.x0, self.y0, self.x0, self.y0)
        self.itemconfig(self.id, fill=color.var.get())
        self.itemconfig(self.id, width=thickness.var.get())

    def move(self, event=None):
        self.x1 = event.x
        self.y1 = event.y
        self.coords(self.id, self.x0, self.y0, self.x1, self.y1)

    def print_msg(self, event):
        print(event)

colors = ('red', 'blue', 'green', 'cyan', 'magenta', 'yellow', 'black')

app = App('Drawing lines on a canvas')
color = Combobox('Color', 'black;red;green;blue;yellow;cyan;magenta')
thickness = Combobox('Thickness', '1;2;5;10;20')

canvas = Canvas(width=600, height=200)

x = 10
d = 20
for col in colors:
    id = canvas.create_rectangle(x, 0, x+d, d, fill=col)
    canvas.tag_bind(id, '<Button-1>', lambda e : print(eval(col)))
    
    x += d

app.run()
