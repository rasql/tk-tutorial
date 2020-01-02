from tklib import *
app = App('set content with listvariable')

App.var = tk.StringVar()

Button('tk', 'App.var.set(dir(tk))')
Button('tk.Button', 'App.var.set(dir(tk.Button))')
Button('tk.Listbox', 'App.var.set(dir(tk.Listbox))')

lb = tk.Listbox(App.stack[-1], listvariable=App.var, height=10)
lb.grid()

app.run()