"""Alert and confirmation dialogs."""

import tkinter as tk
import tkinter.ttk as ttk
from tklib import *
from tkinter import filedialog
from tkinter import messagebox

class Demo(App):
    def __init__(self, **kwargs):
        super(Demo, self).__init__(**kwargs)
        App.root.title('Windows and dialogs')

        Label('Alert and confirmation dialogs', font='Arial 24')

        Button('Show info', 'tk.messagebox.showinfo(message="Hello world")')
        Button('Error', 'tk.messagebox.showinfo(message="Error", icon="error")')
        Button('Question', 'tk.messagebox.showinfo(message="Question", icon="question")')
        Button('Warning', 'tk.messagebox.showinfo(message="Warning", icon="warning")')
        ttk.Separator(App.parent, orient='horizontal').grid()

        types = ('ok', 'okcancel', 'yesno', 'yesnocancel', 'retrycancel', 'abortretryignore')
        for t in types:
            Button(t, 'tk.messagebox.showinfo(message="{}", type="{}")'.format(t, t))
            
if __name__ == '__main__':
    Demo().run()