"""Display tk attributes in a listbox."""

from tklib import *

class Demo(App):
    def __init__(self): 
        super(Demo, self).__init__()

        Label("Tk attributes", font="Arial 18")
        Listbox(dir(tk), height=20, cmd='App.sel["text"] = self.item')

        App.sel = Label('Selection', font='Arial 24')

if __name__ == '__main__':
    Demo().run()