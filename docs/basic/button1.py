"""Create buttons with actions."""
from tklib import *

class Demo(App):
    """Create different buttons."""
    def __init__(self):
        super().__init__()
        App.root.title('Button Demo')
        
        Button()
        Button('Print self', 'print(self)', padding=10)
        Button('Hello', 'print("Hello " * 3)', default='active')

Demo().run()