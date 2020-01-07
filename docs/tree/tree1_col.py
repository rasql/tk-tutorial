from tklib import *
app = App('Treeview - multiple columns')

tree = ttk.Treeview(App.stack[-1])
tree.grid()

tree.insert('', 'end', 'widgets', text='Widgets')
tree.insert('', 0, 'apps', text='Applications')

tree['columns'] = ('size', 'modified')
tree.column('size', width=50, anchor='center')
tree.heading('size', text='Size')
tree.heading('modified', text='Modified')

tree.set('widgets', 'size', '12KB')
tree.set('widgets', 'modified', 'Last week')

tree.insert('', 'end', text='Canvas', values=('25KB Today'))
tree.insert('apps', 'end', text='Browser', values=('115KB Yesterday'))

app.run()