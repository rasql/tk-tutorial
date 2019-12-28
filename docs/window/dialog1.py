"""Standard dialogs."""
from tklib import *

app = App('Standard dialogs')
Label('Standard Dialogs', font='Arial 24')
Button('Open…', 'App.open["text"] = filedialog.askopenfilename()')
App.open = Label('File')

app.run()