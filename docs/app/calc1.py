"""Create calculator buttons."""
from tklib import *

class Demo(App):
    def __init__(self): 
        super(Demo, self).__init__()

        App.lb = Label('0.0')
        App.lb.grid(columnspan=4)

        Button('AC', ).grid(row=1)
        Button('±').grid(row=1, column=1)
        Button('%').grid(row=1, column=2)
        Button(':').grid(row=1, column=3)
        
        Button('7').grid(row=2, column=0)
        Button('8').grid(row=2, column=1)
        Button('9').grid(row=2, column=2)
        Button('x').grid(row=2, column=3)
        
        Button('4').grid(row=3, column=0)
        Button('5').grid(row=3, column=1)
        Button('6').grid(row=3, column=2)
        Button('-').grid(row=3, column=3)
        
        Button('1').grid(row=4, column=0)
        Button('2').grid(row=4, column=1)
        Button('3').grid(row=4, column=2)
        Button('+').grid(row=4, column=3)

        Button('0').grid(row=5, columnspan=2, sticky='we')
        Button('.').grid(row=5, column=2)
        Button('=').grid(row=5, column=3)

if __name__ == '__main__':
    Demo().run()