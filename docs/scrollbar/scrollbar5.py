"""Canvas with a scrollbar."""
from tklib import *

class Canvas(tk.Canvas):
    def __init__(self, scroll='', scrollregion=(0, 0, 1000, 1000), **kwargs):
        self = Scrollable(tk.Canvas, scroll=scroll, scrollregion=scrollregion, **kwargs)

class Demo(App):
    def __init__(self): 
        super().__init__()
        text = 'hello ' * 100
        Label("Canvas with scrollbars", font="Arial 18")
        h = 80

        Label('scroll=')
        Canvas(height=h)
        
        Label('scroll=x')
        Canvas(height=h, scroll='x')

        Label('scroll=y')
        Canvas(height=h, scroll='y')

        Label('scroll=xy')
        Canvas(height=h, scroll='xy')

Demo().run()