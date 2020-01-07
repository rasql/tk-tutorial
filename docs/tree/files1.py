from tklib import *
app = App('File browser')

def cb_open(event):
    print('open', event)

def cb_return(event):
    print('return', event)

cwd = os.getcwd()
Label(cwd)
tree = ttk.Treeview(App.stack[-1])
tree.column('#0', minwidth=300)
tree.bind('<<TreeviewOpen>>', cb_open)
tree.bind('<Return>', cb_return)

Entry('Entry', cmd=cb_return)
Entry('Entry', cmd='print(123)')

dir = os.listdir()
for item in dir:
    size = os.stat(item).st_size
    id = tree.insert('', 'end', text=item, values=(size))
    if os.path.isdir(item):
        tree.insert(id, 0)
    #     sub = os.listdir(item)
    #     for item2 in sub:
    #         size = os.stat(item+'/'+item2).st_size
    #         tree.insert(id, 'end', text=item2, values=(size))

    #     tree['columns'] = ('size')
    #     tree.column('size', width=100, anchor='e')
    #     tree.heading('size', text='Size')
tree.grid()

app.run()