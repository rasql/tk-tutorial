from tklib import *
app = App('Treeview - tags')

tree = ttk.Treeview(App.stack[-1])
tree.grid()

tree.insert('', 'end', text='Item 1', tags=('fg'))
tree.insert('', 'end', text='Item 2', tags=('bg'))
tree.insert('', 'end', text='Item 2')
tree.insert('', 'end', text='Item 4', tags=('fg', 'bg'))

tree.tag_configure('bg', background='yellow')
tree.tag_configure('fg', foreground='red')

app.run()