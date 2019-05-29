from tklib import *

class Demo(App):
    """Write Button and Motion events to statusbar."""
    def __init__(self):
        super(Demo, self).__init__()
        Label("Button and Motion events", font="Arial 24")
        Label('Display the event in the status bar')

        App.root.bind('<Button>', self.cb)
        App.root.bind('<Motion>', self.cb)

    def cb(self, event):
        """Callback function."""
        App.status['text'] = event        
    
if __name__ == '__main__':
    Demo().run()