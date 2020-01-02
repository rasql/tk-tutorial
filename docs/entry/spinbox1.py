from tklib import *

app = App('Spinbox')

var1 = tk.StringVar(value='10')
ttk.Spinbox(App.stack[-1], from_=5.0, to=100.0, increment=25, textvariable=var1).grid()

# default increment=1, from_=0, to=0
var2 = tk.StringVar(value='2')
ttk.Spinbox(App.stack[-1], to=10, textvariable=var2).grid()

# how to use a value list
values = 'Frank;Conny;Jim'.split(';')
var3 = tk.StringVar(value=values[0])
ttk.Spinbox(App.stack[-1], values=values, textvariable=var3).grid()

app.run()