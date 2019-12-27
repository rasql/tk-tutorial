"""Create calculator buttons."""
from tklib import *

class Demo(App):
    def __init__(self): 
        super().__init__()

        s = ttk.Style()
        s.configure('TButton', font='Arial 18', padding=5)

        App.lb = Label('0', font='Arial 36')
        App.lb.grid(columnspan=4, sticky='e')

        Button('C', 'App.lb["text"]  = 0.0').grid(row=1)
        Button('±').grid(row=1, column=1)
        Button('%').grid(row=1, column=2)
        Button(':').grid(row=1, column=3)
        
        Button('7', 'App.lb["text"]  = float(App.lb["text"])*10 + 7').grid(row=2, column=0)
        Button('8', 'App.lb["text"]  = float(App.lb["text"])*10 + 8').grid(row=2, column=1)
        Button('9', 'App.lb["text"]  = float(App.lb["text"])*10 + 9').grid(row=2, column=2)
        Button('x').grid(row=2, column=3)
        
        Button('4', 'App.lb["text"]  = float(App.lb["text"])*10 + 4').grid(row=3, column=0)
        Button('5', 'App.lb["text"]  = float(App.lb["text"])*10 + 5').grid(row=3, column=1)
        Button('6', 'App.lb["text"]  = float(App.lb["text"])*10 + 6').grid(row=3, column=2)
        Button('-').grid(row=3, column=3)
        
        Button('1', 'App.lb["text"]  = float(App.lb["text"])*10 + 1').grid(row=4, column=0)
        Button('2', 'App.lb["text"]  = float(App.lb["text"])*10 + 2').grid(row=4, column=1)
        Button('3', 'App.lb["text"]  = float(App.lb["text"])*10 + 3').grid(row=4, column=2)
        Button('+').grid(row=4, column=3)

        Button('0', 'App.lb["text"]  = float(App.lb["text"])*10 + 0').grid(row=5, columnspan=2, sticky='we')
        Button('.').grid(row=5, column=2)
        Button('=').grid(row=5, column=3)

if __name__ == '__main__':
    Demo().run()