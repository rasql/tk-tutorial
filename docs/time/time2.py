"""Display a timer ."""
from tklib import *
import time

class Clock(Window):
    def __init__(self):
        super(Clock, self).__init__('Clock')
        self.lb = Label('hh:mm:ss', font='Arial 100')
        top = self.lb.winfo_toplevel()
        top.resizable(width=False, height=False)
        self.cb()

    def cb(self, event=None):
        """Display the time every second."""
        t = time.strftime('%X')
        self.lb['text'] = t

        d = time.strftime('%X %x %Z')
        self.status['text'] = d
        self.lb.after(1000, self.cb)

class Timer(Window):
    def __init__(self):
        super(Timer, self).__init__('Timer')
        self.lb = Label('hh:mm:ss', font='Arial 100')
        self.lb.grid(columnspan=4)
        Button('Min').grid(row=1, column=0)
        Button('Sec').grid(row=1, column=1)
        Button('Start').grid(row=1, column=2)
        Button('Reset').grid(row=1, column=3)
        self.cb()

    def cb(self, event=None):
        """Display the time every second."""
        t = time.strftime('%X')
        self.lb['text'] = t

        d = time.strftime('%X %x %Z')
        self.status['text'] = d
        self.lb.after(1000, self.cb)

class Demo(App):
    def __init__(self):
        super().__init__()
        Button('New Clock', Clock)
        Button('New Timer', Timer)

if __name__ == '__main__':
    Demo().run()