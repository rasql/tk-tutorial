"""Create Labels with options."""
from tklib import *

class Demo(App):
    def __init__(self):
        super(Demo, self).__init__()
        Label("Red Text in Times Font", foreground="red", font="Times 24")
        Label("Green Text in Helvetica Font", foreground="green", font="Helvetica 18 bold italic")
        Label("Blue Text in Verdana bold", foreground="blue", font="Verdana 24 bold")
        
if __name__ == '__main__':
    Demo().run()