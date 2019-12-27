from tklib import *

str = """Up until now, we've just dealt with plain text. 
Now it's time to look at how to add special formatting, such as bold, italic, 
and much more. Tk's text widget implements these using a feature called tags.
Tags are objects associated with the text widget. 
Each tag is referred to via a name. 
Each tag can have a number of different configuration options; 
these are things like fonts, colors, etc. that will be used to format text. 
Though tags are objects having state, they don't need to be explicitly created; 
they'll be automatically created the first time the tag name is used.
"""

class Demo(App):
    def __init__(self): 
        super().__init__()
        Label("Formatting with tags", font="Arial 18")

        App.text = Text(str, height=20, width=50)
        App.text.config(undo=True)

        App.text.tag_add('highlight', '5.0', '6.0')
        App.text.tag_add('highlight', '7.0', '7.18')
        App.text.tag_configure('highlight', background='yellow', 
          font='helvetica 14 bold', relief='raised')

        App.text.tag_configure('big', font='helvetica 24 bold', foreground='red')
        App.text.tag_add('big', '8.0', '8.16')

        App.text.insert('end', 'new material ', ('big'))
        App.text.insert('end', 'is ready ', ('big', 'highlight'))
        App.text.insert('end', 'soon', ('highlight'))
    
        b = Button('Popup Menu')
        App.m = ContextMenu(b)
        Item('Item 1', 'print(1)')
        Item('Item 2', 'print(2)')
        Item('Item 3', 'print(3)')
        
        App.text.tag_bind('big', '<1>', App.m.popup)

Demo().run()