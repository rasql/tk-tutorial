"""Regular expression demo."""
from tklib import *
import re

class Demo(App):
    def __init__(self): 
        super().__init__()
        Label('Regular expressions', font='Arial 18')
        Label('Enter a Perl-style regular expression')
        App.re = Entry('regex')

if __name__ == '__main__':
    Demo().run()