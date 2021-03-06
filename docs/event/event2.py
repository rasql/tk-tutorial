"""Write Button and Mouse events to a Text widget."""
from tklib import *

class Demo(App):
    def __init__(self):
        super().__init__()
        Label("Button and Motion events", font="Arial 24")
        App.txt = Text(scroll='y')

        App.root.bind('<Button>', self.cb)
        App.root.bind('<Motion>', self.cb)

    def cb(self, event):
        """Callback function."""
        App.txt.insert('end', str(event) + '\n')
        
if __name__ == '__main__':
    Demo().run()