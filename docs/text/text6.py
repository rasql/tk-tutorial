"""Widgets inside Text widget."""
from tklib import *
import tkinter.ttk as ttk

def hello():
    print('hello')

class Demo(App):
    def __init__(self): 
        super(Demo, self).__init__()
        Label("Widgets inside Text", font="Arial 18")

        App.text = Text(str, height=10)
        b = ttk.Button(App.text, text='Push me', command=hello, padding=10)
        App.text.window_create('1.0', window=b)
        
if __name__ == '__main__':
    Demo().run()