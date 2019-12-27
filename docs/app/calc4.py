"""Create calculator buttons."""
from tklib import *

class Calculator():
    def __init__(self):
        self.win = Window('Calculator')
        s = ttk.Style()
        s.configure('TButton', font='Arial 18', padding=5)

        self.lb = Label('0', font='Arial 44', width=15, anchor='e')
        self.lb.grid(columnspan=4)

        buttons = 'c±%/789*456-123+ 0.='
        for i, b in enumerate(buttons):
            Button(b, lambda c=b: self.calculate(c)).grid(row=i//4+1, column=i%4)
        self.val = 0
        self.pos = 0
        self.val2 = 0
        self.op = ''

        self.win.top.bind('<Key>', self.cb)

    def cb(self, event=None):
        """React to key press events."""
        c = event.char
        if c != '':
            self.calculate(c)

    def calculate(self, c):
        """Calculator for 4 basic operations."""
        if c in '0123456789.±+-/*%c=':
            if c in '0123456789':
                if self.pos:
                    self.val += int(c) * 10**self.pos
                    self.pos -= 1
                else:
                    self.val *= 10
                    self.val += int(c)
            elif c == '.':
                self.pos = -1
            elif c == '%':
                self.val *= 0.01
            elif c == '±':
                self.val *= -1
            elif c in '+-/*':
                self.val2 = self.val
                self.val = 0
                self.pos = 0
                self.op = c
            elif c == '=':
                e = str(self.val2) + self.op + str(self.val)
                self.val = eval(e)
            if c == 'c':
                self.val = 0
                self.pos = 0

            self.lb['text'] = self.val


class Demo(App):
    def __init__(self): 
        super().__init__()
        Button('New calculator', Calculator)
        Menu('App')
        Item('Calculator', Calculator)

if __name__ == '__main__':
    Demo().run()