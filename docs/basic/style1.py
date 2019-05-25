"""Using themes and styles."""

import tkinter as tk
import tkinter.ttk as ttk
from tklib import *

class Demo(App):
    def __init__(self, **kwargs):
        super(Demo, self).__init__(**kwargs)
        Label('Themes', font='Arial 24')
        
        s = ttk.Style()
        print(s.layout('TButton'))

        themes = s.theme_names()
        Combobox(themes, 'ttk.Style().theme_use(self.item)')

        for t in themes:
            s.theme_use(t)
            Button(t)

if __name__ == '__main__':
    Demo().run()