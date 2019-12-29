"""Create checkbuttons."""
from tklib import *

app = App()
Checkbutton('English;German;French', 'print(self.selection)')
app.run()