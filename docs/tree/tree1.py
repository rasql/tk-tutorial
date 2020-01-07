from tklib import *

def itemClicked(event):
    print(event)
    print(tree.focus())

app = App('Treeview')

tree = ttk.Treeview(App.stack[-1])
tree.grid()

tree.insert('', 'end', 'widgets', text='Widget Tour')
tree.insert('', 0, 'gallery', text='Applications')

id = tree.insert('', 'end', text='Tutorial')

# Inserted underneath an existing node:
tree.insert('widgets', 'end', text='Canvas')
tree.insert(id, 'end', text='Tree')

tree['columns'] = ('size', 'modified', 'owner')
tree.column('size', width=50, anchor='center')
tree.heading('size', text='Size')
tree.heading('modified', text='Modified')

tree.set('widgets', 'size', '12KB')
size = tree.set('widgets', 'size')
tree.insert('', 'end', text='Listbox', values=('15KB Yesterday mark'))
tree.insert('', 'end', text='Canvas', values=('25KB Today raph'))

tree.insert(id, 'end', text='button', tags=('ttk', 'simple'))
tree.tag_configure('ttk', background='yellow')
tree.tag_configure('simple', foreground='red')
tree.tag_bind('ttk', '<1>', itemClicked)
app.run()