from tklib import *
app = App('Combobox')

Combobox('Weekday', 'Mon;Tue;Wed;Thu;Fri', 'print(self.item)')
Combobox('Country', 'Switzerland;France;Italy;Germany', 'print(self.item)')
Combobox('Year', [2005, 2006, 2007], 'print(self.item)')
Combobox('Integer', list(range(10)), 'print(self.item)')

app.run()