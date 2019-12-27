"""Create checkboxes."""
from tklib import *

class Demo(App):
    def __init__(self):
        super().__init__()
        Label('Checkbox Demo', font='Arial 24')

        Label('Select your favorite languages')
        Checkbox('Python;Perl;Ruby;Java;C++', 'print(self.selection)')

Demo().run()