"""Insert items to the tree."""

from tklib import *

class Demo(App):
    def __init__(self): 
        super(Demo, self).__init__()
        Label('Insert items to the tree', font='Arial 24')
        
        App.text = Entry('Text', 'print(self.val.get())')
        App.index = Spinbox('Index', 'print(self.val.get())', to=100)
        
        Button('Insert', 'App.tree.insert("", App.index.val.get(), text=App.text.get())')
        Button('Insert to Folder', 'App.tree.insert("folder", App.index.val.get(), text=App.text.get())')

        App.tree = Treeview()

        L = 'Hello;Dolly;How;Are;You'.split(';')
        for item in L:
            App.tree.insert('', 'end', text=item)
        App.tree.insert('', 0, 'folder', text='Folder')
  
if __name__ == '__main__':
    Demo().run()