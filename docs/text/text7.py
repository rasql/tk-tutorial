"""Search in text."""
from tklib import *

str = """Up until now, we've just dealt with plain text. 
Now it's time to look at how to add special formatting, such as bold, italic, 
strikethrough, background colors, font sizes, and much more. Tk's text widget 
implements these using a feature called tags.
Tags are objects associated with the text widget. 
Each tag is referred to via a name chosen by the programmer. 
"""

def highlight():
    sel = App.text.tag_ranges('sel')
    if len(sel) > 0:
        App.text.tag_add('highlight', *sel)

def search(event=None):
    App.text.tag_remove("highlight", "1.0", "end")
    start = 1.0
    while True:
        pattern = App.re.val.get()
        pos = App.text.search(pattern, start, stopindex='end', regexp=True)
        if not pos:
            break
        print(pos)
        App.text.tag_add('highlight', pos, pos+'+1c')
        start = pos + '+1c'

class Demo(App):
    def __init__(self): 
        super(Demo, self).__init__()
        Label("Search with regexp", font="Arial 18")

        App.text = Text(str, height=10)
        App.text.tag_configure('highlight', background='yellow')

        App.re = Entry('search', search)
             
Demo().run()