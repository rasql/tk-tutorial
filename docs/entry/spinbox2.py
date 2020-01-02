from entry import *
app = App('Spinbox')

Spinbox('values=(1, 2, 5, 50)', values=(1, 2, 5, 10), val=5)
Spinbox('from_=-5, to=5', from_=-5, to=5, wrap=True)
Spinbox('to=5, wrap=True', to=5, wrap=True)
Spinbox('to=50, increment=5', to=50, increment=5)
Spinbox('to=1, increment=0.1', to=1, increment=0.1)
Spinbox('<Return> self.configure()', 'print(self.configure())')
Spinbox('<Return> self.var.get()', 'print(self.var.get())', to=5)
Spinbox('state=disabled', to=5, state='disabled', val=2)
Spinbox('state=readonly', to=5, state='readonly', val=2)
app.run()