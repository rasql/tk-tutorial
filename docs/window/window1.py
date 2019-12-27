"""Open multiple windows."""
from tklib import *

class Demo(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        App.root.title('Windows and dialogs')

        Button('New Window', 'Window()')
        Button('Print window geometry', 'print(App.root.geometry())')
        Button('Print window title', 'print(App.root.title())')
        Separator()
        
        Button('Resize H', 'App.root.resizable(True, False)')
        Button('Resize V', 'App.root.resizable(False, True)')
        Button('Iconify', 'App.root.iconify()')
         
        Window('Text')
        Text(height=10, width=40)

        Window('Canvas')
        Canvas()

Demo().run()