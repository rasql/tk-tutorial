from entry import *

app = App('Scale')      
Scale('Scale', 'print(self.var.get())', to=10, length=200)
Scale('from=-50, to=50', 'print(self.var.get())', from_=-50, to=50)

app.run()