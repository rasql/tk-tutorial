"""Display Spinbox widgets."""

from tklib import *

class Demo(App):
    def __init__(self): 
        super().__init__()
        Label("Spinbox", font="Arial 18")

        Label('values=(1, 2, 5, 10, 20, 50)')
        Spinbox(values=(1, 2, 5, 10, 20, 50))

        Label('from_=-10, to=10')
        Spinbox(from_=-10, to=10)

        Label('to=5, wrap=True')
        Spinbox(to=5, wrap=True)

        Label('to=50, increment=5')
        Spinbox(to=50, increment=5)

        Label('to=1.0, increment=0.1')
        Spinbox(to=1.0, increment=0.1)

        Label('<Return> configure()')
        Spinbox(cmd='print(self.configure())')

        Label('<Return> self.val.get()')
        Spinbox(cmd='print(self.val.get())')

if __name__ == '__main__':
    Demo().run()