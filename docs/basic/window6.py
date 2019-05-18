"""Paned windows."""

from tklib import *

class Demo(App):
    def __init__(self, **kwargs):
        super(Demo, self).__init__(**kwargs)
        App.root.title('Paned windows')

        Label('Paned windows', font='Arial 24')
        Separator()

        Button('New button', 'Button()')
        Button('New label', 'Label()')
        Button('New separator', 'Separator()')
        Separator()

        p=Pandedwindow(orient='horizontal')
        f=Labelframe(text='Pane 1', height=200)
        Button()
        Label()

        App.parent = App.stack.pop()
    
        f2=Labelframe(text='Pane 2', height=200)
        Button()
        Label()

        p.add(f)
        p.add(f2)
            
if __name__ == '__main__':
    Demo().run()