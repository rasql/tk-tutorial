"""Create radio buttons."""

from tklib import *

class Demo(App):
    def __init__(self):
        super(Demo, self).__init__()
        Label('Radiobutton demo', font='Arial 24')

        Label('Select your favorite programming language')
        Radiobutton('Python;Perl;Ruby;Java;C++', 'print(self.item)')
        
        Label('Select your favorite day of the week')
        Radiobutton('Mon;Tue;Wed;Thu;Fri', 'print(self.item)')
    
if __name__ == '__main__':
    Demo().run()