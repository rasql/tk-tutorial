from tklib import *
app = App('Treeview - bind')

def cb(event):
    print(event, tree.selection(), tree.focus())

tree = ttk.Treeview(App.stack[-1])
tree.grid()

tree.insert('', 'end', text='Item 1', tags=('cb'))
id = tree.insert('', 'end', text='Item 2', tags=('cb'))
tree.insert(id, 'end', text='Sub-Item 1', tags=('cb'))
tree.insert(id, 'end', text='Sub-Item 2', tags=('cb'))

tree.tag_bind('cb', '<1>', cb)
tree.tag_bind('cb', '<<TreeviewSelect>>', cb)
tree.tag_bind('cb', '<<TreeviewOpen>>', cb)
tree.tag_bind('cb', '<<TreeviewClose>>', cb)

app.run()