import tkinter as tk
import tkinter.ttk as ttk
from tklib import *

class Demo(App):
    def __init__(self, **kwargs):
        super(Demo, self).__init__(**kwargs)
        App.root.title('Label Demo')

        Fr(borderwidth=4, relief='solid', width=300)
        Label('First\nname:', padding=5, foreground='red', background='yellow', anchor='w')
        Label('Last\nname:', font='Arial 36', foreground='green', borderwidth=10, relief='sunken')

        Fr(borderwidth=10, relief='sunken')
        Label('First\nname:', padding=50, foreground='green', justify='right', anchor='e')
        Label('Last name:', font='Arial 36', foreground='blue', padding=20)

        App.parent = App.stack.pop()
        App.parent = App.stack.pop()

        Fr(borderwidth=10, relief='raised')
        Label('First name:', padding=(50, 10), foreground='red', background='yellow')
        Label('Last name:', font='Arial 36', foreground='blue', padding=20)

        img = tk.PhotoImage(file='icons/bag.png')
        w = Label('Address:')
        w['image'] = img
        w['compound'] = 'top'
        print(w)
        print(w['compound'])
    
if __name__ == '__main__':
    Demo().run()