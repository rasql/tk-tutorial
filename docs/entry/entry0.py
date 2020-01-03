from entry import *

app = App('Entry, Combobox, Spinbox')

Entry('Entry', val='enter text')
Combobox('Combobox', 'select item;item 2')
Spinbox('Spinbox', val=5, to=10)
Scale('Scale')

app.run()