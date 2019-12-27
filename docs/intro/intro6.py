"""Create radio buttons."""
from tklib import *

class Demo(App):
    def __init__(self):
        super().__init__()
        Label('Radiobutton demo', font='Arial 24')

        Label('Select your favorite programming language')
        Radiobutton('Python;Perl;Ruby;Java;C++', 'print(self.item)')
    
Demo().run()