from tklib import *

app = App('insert and delete')
App.var = tk.StringVar()

Button('Insert 1', 'App.lb.insert(tk.END, "new item 1")')
Button('Insert 2', 'App.lb.insert(tk.END, "new item 2")')

Button('Delete first', 'App.lb.delete(0)')
Button('Delete last', 'App.lb.delete(tk.END)')
Button('Delete all', 'App.lb.delete(0, tk.END)')

App.lb = tk.Listbox(App.stack[-1], listvariable=App.var, height=10)
App.lb.grid()

app.run()