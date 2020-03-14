from tklib import *

def cb(event):
    """Callback function."""
    print(event)  

app = App('Events and bindings')

Label("Button and Motion events", font="Arial 24")
Label('Display the event in the status bar')

app.root.bind('<Button>', cb)
app.root.bind('<Motion>', cb)

app.run()