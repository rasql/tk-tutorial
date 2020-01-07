from tklib import *
app = App('Entry widgets')

Entry('Entry', 'print(self.var.get())')
Entry('', 'print(self.var.get())', val='inital value', width=10)
Combobox('Combobox', 'Item 1;Item 2;Item 3', 'print(self.var.get())')
Combobox('', 'Item 1;Item 2;Item 3',
            'print(self.var.get())', val=2, width=10)
Spinbox('Spinbox', to=10, val=5)
Spinbox('', 'print(self.var.get())', to=10, width=10)
Scale('Scale', 'print(self.var.get())', to=10, val=5)
Scale(cmd='print(self.var.get())', to=100, length=100)

app.run()