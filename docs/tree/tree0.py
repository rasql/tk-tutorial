from tklib import *
app = App('Treeview')

tree = ttk.Treeview(App.stack[-1])
tree.grid()
tree.insert('', 0, text='Item 1')
tree.insert('', 'end', text='Item 2')

id = tree.insert('', 5, text='Item 3')
tree.insert(id, 0, text='sub-item 0')
tree.insert(id, 1, text='sub-item 1')
app.run()