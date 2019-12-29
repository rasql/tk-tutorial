from tklib import *
app = App('Checkbuttons')

Label('Select your favorite languages')
Checkbutton('Python;Perl;Ruby;Java;C++', 'print(self.selection)')

app.run()