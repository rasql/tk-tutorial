"""Buttons which create other buttons."""
from tklib import *

class Demo(App):
    """Create different buttons."""
    def __init__(self):
        super().__init__()
        App.root.title('Button Demo')
        
        Button('Add Button', 'Button()')
        Button('Add self-destroy button', 'Button("Destroy", "self.destroy()")')

Demo().run()