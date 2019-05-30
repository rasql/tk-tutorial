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

def big():
    sel = App.text.tag_ranges('sel')
    if len(sel) > 0:
        App.text.tag_add('big', *sel)

class Demo(App):
    def __init__(self): 
        super(Demo, self).__init__()
        Label("Formatting with tags", font="Arial 18")

        App.text = Text(str, height=10)
        App.text.tag_configure('highlight', background='yellow')
        App.text.tag_configure('big', font='helvetica 24')
        
        Button('Selection range', 'print(App.text.tag_ranges("sel"))')
        Button('Highlight ranges', 'print(App.text.tag_ranges("highlight"))')
        Button('Big ranges', 'print(App.text.tag_ranges("big"))')
        Button('Mark names', 'print(App.text.mark_names())')
        
        Button('Highlight', highlight)
        Button('Big', big)
        
if __name__ == '__main__':
    Demo().run()