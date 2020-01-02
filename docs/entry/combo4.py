from tklib import *
app = App('Combobox')

def cb(e=None):
    print(c1.var.get())

Combobox('string - "1;2;3"', '1;2;3')
Combobox('tuple - (1, 2, 3)', (1, 2, 3))
Combobox('list - [1, 2, 3]', [1, 2, 3])
Combobox('range(100)', list(range(100)))
Combobox('width=10', '1;2;3', width=10)

c1 = Combobox('cmd function', (1, 2, 3), cb)
Combobox('cmd string', (1, 2, 3), 'print(self.item)')
Combobox(values='a;b;c', cmd='print(self.item)')
Combobox(values='a;b;c', cmd='print(self.item)', width=10)

app.run()