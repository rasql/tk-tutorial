"""Display tk Text."""
from tklib import *

class Demo(App):
    def __init__(self): 
        super().__init__()
        Label("Text widget", font="Arial 18")

        Label('2 lines')
        Text('Initial text...', height=2, width=50)

        Label('10 lines')
        text = Text(height=10, width=50)
        text.insert('1.0', 'Add some text at the beginning of the Text widget.')

Demo().run()