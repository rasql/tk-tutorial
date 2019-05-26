"""Places embedded frames."""

from tklib import *

class Demo(App):
    def __init__(self):
        super(Demo, self).__init__()
        Label('Template', font='Arial 24')

        f = Frame(borderwidth=2, relief='raised')
        print('frame style', f['style'])

        Button()
        Label()
        Entry()

if __name__ == '__main__':
    Demo().run()