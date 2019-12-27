"""Help browser."""
from tklib import *

class Demo(App):
    def __init__(self): 
        super().__init__()
        Label("Help display", font="Arial 24")

        str = tk.__doc__
        App.text = Text(str)
             
Demo().run()