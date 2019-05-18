"""Separators and Labelframes."""

from tklib import *

class Demo(App):
    def __init__(self, **kwargs):
        super(Demo, self).__init__(**kwargs)
        App.root.title('Windows and dialogs')

        Label('Separators and Labelframes', font='Arial 24')
        Separator()

        Button('New button', 'Button()')
        Button('New label', 'Label()')
        Button('New separator', 'Separator()')
        Separator()

        Labelframe(text='Frame 1', padding=5)
        Button()
        Label()

        App.parent = App.stack.pop()

        Labelframe(text='Frame 2', padding=5)
        Button()
        Label()
            
if __name__ == '__main__':
    Demo().run()