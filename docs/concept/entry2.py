from tklib import *

class Demo(App):
    """Convert between feet and meters"""
    def __init__(self): 
        super().__init__()

        Label('Convert between feet and meters', font="Arial 18")
        Label('Enter value and hit ENTER')

        App.m = Entry('feet', 'App.f.val.set(float(self.val.get())*0.3048)')
        App.f = Entry('meters', 'App.m.val.set(float(self.val.get())/0.3048)')

if __name__ == '__main__':
    Demo().run()