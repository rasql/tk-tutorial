from tklib import *
import re
app = App('Regular expression')

Label('Regular expressions', font='Arial 18')
Label('Enter a Perl-style regular expression')
App.re = Entry('regex')

app.run()