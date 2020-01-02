from tklib import *
app = App('Combobox')

Combobox('dir(tk)', dir(tk), 'print(self.item); App.entry.var.set(eval("tk."+self.item))')
App.entry = Entry('value')
Combobox('dir(ttk)', dir(ttk), 'print(eval("ttk."+self.item))')

app.run()