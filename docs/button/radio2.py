"""Create radio buttons."""
from tklib import *

app = App()
Radiobutton('English;German;French', 'print(self.item)')
app.run()