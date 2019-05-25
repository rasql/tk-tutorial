"""Insert multiple columns to the tree."""

from tklib import *

class Demo(App):
    def __init__(self): 
        super(Demo, self).__init__()
        Label('Columns', font='Arial 24')
         
        App.tree = Treeview()
        # App.tree['columns'] = ('size', 'date', 'type')
        App.tree['columns'] = range(3)

        App.text = Entry('Text', 'print(self.val.get())')
        App.row = Spinbox('Row:', 'print(self.val.get())', to=100)
        App.col = Spinbox('Column:',  'print(self.val.get())', to=100)
        Button('Set', 'App.tree.set(App.tree.focus(), App.col.val.get(), App.text.get())')

        for i in range(2):
            App.tree.column(i, width=100, anchor='w')
            App.tree.heading(i, text='Heading' + str(i))

        L = 'Hello;Dolly;How;Are;You'.split(';')
        for item in L:
            App.tree.insert('', 'end', text=item)
  
if __name__ == '__main__':
    Demo().run()