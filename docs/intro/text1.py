"""Display tk Text."""

from tklib import *

class Demo(App):
    def __init__(self): 
        super(Demo, self).__init__()
        Label("Text widget", font="Arial 18")

        t = tk.Text(App.parent, height=10)
        t.insert('1.0', 'add some text at the beginning of the Text widget.')
        t.grid()

if __name__ == '__main__':
    Demo().run()