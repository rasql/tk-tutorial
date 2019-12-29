from tklib import *
app = App('Radio buttons')

Label('Select your favorite programming language')
Radiobutton('Python;Perl;Ruby;Java;C++', 'print(self.item)')

app.run()