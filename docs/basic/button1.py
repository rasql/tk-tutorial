import tkinter as tk
from tklib import *

class Demo(App):
    """Create different buttons."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        App.root.title('Button Demo')
        
        Button()
        Button('Print 123', 'print(123)', padding=10)
        Button('Hello', 'print("Hello " * 3)', default='active')
        Button('Add Button', 'Button()')
        Button('Add self-destroy button', 'Button("Destroy", "self.destroy()")')
        Button('Print self', 'print(self)')
        Button('Print self', 'print(self)')
        b = Button('Image')

        img = tk.PhotoImage(file='basic/icons/bag.png')
        b['image'] = img
        b['compound'] = 'top'

if __name__ == '__main__':
    Demo().run()