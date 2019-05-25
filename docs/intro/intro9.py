"""Create a combobox."""

from tklib import *

class Demo(App):
    def __init__(self):
        super(Demo, self).__init__()
        Label('Combobox', font='Arial 24')
        Combobox('Weekday', 'Mon;Tue;Wed;Thu;Fri', 'print(self.item)')
        Combobox('Country', 'Switzerland;France;Italy;Germany', 'print(self.item)')
        Combobox('Year', ['2005', '2006', '2007'], 'print(self.item)')
        Combobox('Integer', list(range(10)), 'print(self.item)')

if __name__ == '__main__':
    Demo().run()