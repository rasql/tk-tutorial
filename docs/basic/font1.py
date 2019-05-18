"""Standard fonts."""

from tklib import *

class Demo(App):
    def __init__(self, **kwargs):
        super(Demo, self).__init__(**kwargs)
        App.root.title('Windows')

        Label('Standard fonts', font='Arial 24')

        fonts = ['TkDefaultFont', 'TkTextFont', 'TkFixedFont', 'TkMenuFont', 'TkHeadingFont']
        for x in fonts:
            Label(x, font=x+' 18')


        fonts = ['Times', 'Courier', 'Helvetica']
        for x in fonts:
            Label(x, font=x+' 18')

if __name__ == '__main__':
    Demo().run()