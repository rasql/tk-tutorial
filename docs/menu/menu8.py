"""Insert widgets via a menu."""

from tklib import *

class Demo(App):
    def __init__(self):
        super().__init__()
        Label("Insert widgets via the menu.", font="Arial 24")

        Menu('Widgets')
        Item('Button', 'Button()', 'Command-b')
        Item('Label', 'Label()', 'Command-l')
        Item('Entry', 'Entry()', 'Command-e')
        Item('Radiobutton', 'Radiobutton()', 'Command-r')
        Item('Checkbox', 'Checkbox()', 'Command-k')
        Item('Canvas', 'Canvas()', 'Command-c')
        Item('Listbox', 'Listbox(height=5)', 'Command-i')
        Item('Scale', 'Scale()', 'Command-s')
        Item('Text', 'Text(width=30, height=5)', 'Command-t')

if __name__ == '__main__':
    Demo().run()