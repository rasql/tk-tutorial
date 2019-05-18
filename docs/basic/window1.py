"""Open multiple windows."""

import tkinter as tk
import tkinter.ttk as ttk
from tklib import *

class Demo(App):
    def __init__(self, **kwargs):
        super(Demo, self).__init__(**kwargs)
        App.root.title('Windows and dialogs')
        Button('New Window', 'Window()')
        Button('Add Button', 'Button(cmd="print(self)")')
        Button('Add Label', 'Label()')
        Button('Add Destroy Button', 'Button("Destroy", "self.destroy()")')
        Button('Print window geometry', 'print(App.root.geometry())')
        Button('Print window title', 'print(App.root.title())')
        Button('Resize H', 'App.root.resizable(True, False)')
        Button('Resize V', 'App.root.resizable(False, True)')
        Button('Iconify', 'App.root.iconify()')
         
        Window('First')
        Button('First')
        Label('First')

        Window('Second')

if __name__ == '__main__':
    Demo().run()