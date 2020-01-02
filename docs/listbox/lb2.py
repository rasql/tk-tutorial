from tklib import *
app = App('insert and delete')
var = tk.StringVar(value=dir(tk))

def configure():
    i = int(index.var.get())
    bg = background.var.get()
    listbox.itemconfigure(i, background=bg)

index = Entry('index', 'print(self.var.get())', val=3)
background = Entry('background', 'print(self.var.get())', val='#f0f0ff')
Button('Configure', configure)

listbox = tk.Listbox(App.stack[-1], listvariable=var, height=10)
listbox.grid()

app.run()