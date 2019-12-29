"""Custumize the Treeview widget."""

from tklib import *

class Demo(App):
    def __init__(self): 
        super().__init__()
        Label('Customizing the Treeview widget', font='Arial 24')
        
        App.tree = Treeview()
        App.tree['columns'] = range(3)

        Spinbox('height=', 'App.tree["height"]=self.val.get()')
        Spinbox('width=', 'App.tree.column("#0", width=self.val.get())', inc=50, to=500)
        Spinbox('width 0=:', 'App.tree.column(0, width=self.val.get())', inc=50, to=500)
        Spinbox('width 1=:', 'App.tree.column(1, width=self.val.get())', inc=50, to=500)
        Combobox('selectmode=', 'browse;extended;none', 'App.tree["selectmode"]=self.val.get()')
        Button('show tree', "App.tree['show']='tree'")
        Button('show headings', "App.tree['show']='headings'")
        Checkbutton('tree;headings')
        
        for i in range(2):
            App.tree.column(i, width=100, anchor='w')
            App.tree.heading(i, text='Heading' + str(i))

        L = 'Hello;Dolly;How;Are;You'.split(';')
        for item in L:
            App.tree.insert('', 'end', text=item)
  
if __name__ == '__main__':
    Demo().run()