"""Draw lines, ovals and text on a canvas."""
from tklib import *

class Demo(App):
    def __init__(self):
        super(Demo, self).__init__()
        Label("Canvas", font="Arial 24")

        c = Canvas(width=600, height=300, background='lightblue')
        
        c.create_line(10, 10, 200, 200, fill='red')
        c.create_line(20, 10, 210, 200, fill='blue', width=3)
        c.create_oval(100, 200, 150, 250, fill='green', width=2)
        c.create_oval(300, 100, 580, 250, fill='yellow', width=5)
        c.create_text(300, 150, text="Python", font='Arial 48')
        c.create_text(300, 250, text="Canvas", font='Zapfino 72')

Demo().run()