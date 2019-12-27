"""Alert and confirmation dialogs."""
from tklib import *
from tkinter import filedialog, messagebox

class Demo(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Label('Alert and confirmation dialogs', font='Arial 24')

        Button('Show info', 'tk.messagebox.showinfo(message="Hello world")')
        Button('Error', 'tk.messagebox.showinfo(message="Error", icon="error")')
        Button('Question', 'tk.messagebox.showinfo(message="Question", icon="question")')
        Button('Warning', 'tk.messagebox.showinfo(message="Warning", icon="warning")')
        Separator()

        types = ('ok', 'okcancel', 'yesno', 'yesnocancel', 'retrycancel', 'abortretryignore')
        for t in types:
            Button(t, 'tk.messagebox.showinfo(message="{}", type="{}")'.format(t, t))
            
Demo().run()