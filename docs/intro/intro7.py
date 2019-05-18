"""Create checkboxes."""

from tklib import *

class Demo(App):
    def __init__(self):
        super(Demo, self).__init__()
        Label('Checkbox Demo', font='Arial 24')

        Label('Select your favorite languages')
        Checkbox('Python;Perl;Ruby;Java;C++', 'print(self.selection)')
        
        Label('Select your working days')
        Checkbox('Mon;Tue;Wed;Thu;Fri', 'print(self.selection)')

if __name__ == '__main__':
    Demo().run()