"""Change the cursor."""

from tklib import *

cursors = [
    "arrow", 
    "circle",
    "clock",
    "cross",
    "dotbox",
    "exchange",
    "fleur",
    "heart",
    "man",
    "mouse",
    "pirate",
    "plus",
    "shuttle",
    "sizing",
    "spider",
    "spraycan",
    "star",
    "target",
    "tcross",
    "trek",
    "watch",
]

class Demo(App):
    def __init__(self): 
        super().__init__()
        Label('Cursors', font='Arial 24')

        for x in cursors:
            Button(x, cursor=x)

if __name__ == '__main__':
    Demo().run()