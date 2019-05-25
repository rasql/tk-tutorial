"""Use Entry widget."""

from tklib import *

class Demo(App):
    def __init__(self): 
        super(Demo, self).__init__()

        App.l = Label("Get widget value", font="Arial 18")

        Button('My Button', 'print(self["text"])')
        Checkbox('A;B;C', 'print(self.selection)')
        Combobox('Combobox', '1;2;5;10', 'print(self.val.get())')
        Entry('Entry', 'print(self.get())')
        Label('My Label')
        Radiobutton('A;B;C', 'print(self.val.get(), self.item)')
        Scale()
        Spinbox('Spinbox', 'print(self.val.get())')

if __name__ == '__main__':
    Demo().run()