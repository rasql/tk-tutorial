"""Paned windows."""
from tklib import *

class Demo(App):
    def __init__(self, **kwargs):
        super(Demo, self).__init__(**kwargs)
        Label('Paned windows', font='Arial 24')

        p = Panedwindow(orient='horizontal')
        print(p)
        f1 = Canvas(background='pink')
        f2 = Canvas(background='lightblue')
        p.add(f1)
        p.add(f2)

        App.stack.pop()
        Label('Another paned window')

        p2 = Panedwindow(orient='horizontal')
        print(p2)
        p2.add(Canvas(background='yellow'))
        p2.add(Canvas(background='lightgreen'))
        p2.add(Canvas(background='orange'))

        # p=Panedwindow(orient='horizontal')
        # f=Labelframe(text='Pane 1', height=200)
        # Button()
        # Label()
    
        # f2=Labelframe(text='Pane 2', height=200)
        # Button()
        # Label()

        # p.add(f)
        # p.add(f2)
            
if __name__ == '__main__':
    Demo().run()