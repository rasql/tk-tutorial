"""Display a clock ."""

from tklib import *
import time

class Clock():
    def __init__(self):
        Window('Clock')
        self.lb = Label('hh:mm:ss', font='Arial 100')
        self.cb()

    def cb(self, event=None):
        t = time.strftime('%X')
        self.lb['text'] = t

        d = time.strftime('%X %x %Z')
        App.status['text'] = d
        self.lb.after(1000, self.cb)

class Demo(App):
    def __init__(self):
        super(Demo, self).__init__()
        Button('New Clock', Clock)
        Clock()


if __name__ == '__main__':
    Demo().run()