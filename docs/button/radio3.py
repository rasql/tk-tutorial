"""Create radio buttons."""
from tklib import *

app = App()
Radiobutton('English;German;French;Italian', 'print(self.item)', 2)
app.run()