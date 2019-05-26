"""Display tk Text."""

from tklib import *

class Demo(App):
    def __init__(self): 
        super(Demo, self).__init__()
        Label("Text widget", font="Arial 18")

        Spinbox('width', 'App.text["width"]=self.val.get()').set(80)
        Spinbox('height', 'App.text["height"]=self.val.get()').set(4)
        
        App.text = Text('Initial text...', height=2)

if __name__ == '__main__':
    Demo().run()