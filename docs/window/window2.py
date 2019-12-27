"""Standard dialogs."""
from tklib import *
from tkinter import filedialog, colorchooser

class Demo(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        App.root.title('Windows and dialogs')
        Label('Standard Dialogs', font='Arial 24')

        Button('Open…', 'App.open["text"] = tk.filedialog.askopenfilename()')
        App.open = Label('File')

        Button('Save…', 'App.save["text"] = tk.filedialog.asksaveasfilename()')
        App.save = Label('File')

        Button('Directory', 'App.dir["text"] = tk.filedialog.askdirectory()')
        App.dir = Label('Directory')

        Button('Select color…', 'App.col["text"] = tk.colorchooser.askcolor()')
        App.col = Label('Color')

Demo().run()