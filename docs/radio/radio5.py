from tklib import *

app = App('Radiobuttons')
Radiobutton()                           # no item list
Radiobutton('A;B', 'print(self.item')   # error in command
Radiobutton('a;b', 'print(self.item)')  # correct

app.run()