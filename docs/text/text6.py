"""Widgets inside Text"""
from tklib import *

def hello():
    print('hello')

class Demo(App):
    def __init__(self): 
        super().__init__()
        Label("Widgets inside Text", font="Arial 18")

        App.text = Text(str, height=10, width=50)
        b = ttk.Button(App.text, text='Push me', command=hello, padding=10)
        App.text.window_create('1.0', window=b)
        
Demo().run()