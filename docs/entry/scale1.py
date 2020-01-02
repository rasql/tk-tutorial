from tklib import *

app = App('Scale')      
ttk.Scale(App.stack[-1]).grid()
ttk.Scale(App.stack[-1], length=200, to=100).grid()
ttk.Scale(App.stack[-1], length=300, from_=-100, to=100).grid()
app.run()