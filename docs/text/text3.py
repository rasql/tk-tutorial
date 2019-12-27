"""Undo and Redo."""
from tklib import *

class Demo(App):
    def __init__(self): 
        super().__init__()
        Label("Undo and Redo", font="Arial 18")

        App.text = Text('Initial text...', height=10, width=50)
        App.text.config(undo=True)

        Button('Selection')
        Button('Edit Undo', 'App.text.edit_undo()')
        Button('Edit Redo', 'App.text.edit_redo()')
        Inspector(App.text, height=20)

Demo().run()