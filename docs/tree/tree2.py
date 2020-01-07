from tklib import *

app = App('Treeview')

items = dir(tk)
tree = Treeview()
tree['columns'] = ('type', 'value')
tree.column('type', width=100)
tree.heading('type', text='Type')
tree.heading('value', text='Value')

for item in items:
    x = eval('tk.'+item)
    t = type(x)
    print(t.__name__, x)
    tree.insert('', 'end', text=item, values=(t.__name__, x))

items = dir()
Treeview(items).grid(row=0, column=1)

app.run()