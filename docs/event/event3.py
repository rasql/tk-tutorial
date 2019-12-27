from tklib import *

class Demo(App):
    """Write Enter, Leave and Return events to a Text widget."""
    def __init__(self):
        super().__init__()
        Label("Enter, Leave and Return events", font="Arial 24")
        
        App.txt = Text()
        App.txt.grid(sticky='nswe')

        App.root.bind('<Enter>', self.cb)
        App.root.bind('<Leave>', self.cb)
        App.root.bind('<Return>', self.cb)
        App.root.bind('<Configure>', self.cb)

    def cb(self, event):
        """Callback function."""
        App.txt.insert('end', str(event) + '\n')
        
if __name__ == '__main__':
    Demo().run()