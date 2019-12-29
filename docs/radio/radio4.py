from tklib import *

app = App('Radiobuttons')
Radiobutton('English;German;French;Italian', 'print(self.item)', 2)
app.run()