"""Show different fonts."""
from tklib import *

class Demo(App):
    def __init__(self):
        super().__init__()

        fonts = ['Times', 'Courier', 'Helvetica', 'Didot']
        for x in fonts:
            Label(x, font=x+' 36')

Demo().run()