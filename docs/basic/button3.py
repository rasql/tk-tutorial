"""Add buttons and introspect."""

import tkinter as tk
import tkinter.ttk as ttk
from tklib import *

class Demo(App):
    def __init__(self, **kwargs):
        super(Demo, self).__init__(**kwargs)
        Label('Adding Buttons', font='Arial 24')

        Button('Add Button', 'Button(cmd="print(self)")')
        Button('Add Destroy Button', 'Button("Destroy", "self.destroy()")')
        Button('print(self)', 'print(self)')
        Button('Add Label', 'Label()')
        Separator()


if __name__ == '__main__':
    Demo().run()