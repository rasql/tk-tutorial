"""Use styles and themes."""

import tkinter as tk
import tkinter.ttk as ttk
from tklib import *

# class Frame(ttk.Frame):
#     def __init__(self, **kwargs):
#         super(Frame, self).__init__(App.stack[-1], borderwidth=1, relief='solid', **kwargs)
#         App.stack.append(self)
#         self.grid()

class Demo(App):
    def __init__(self):
        super(Demo, self).__init__()
        Label('Widget style', font='Arial 24')

        Label('widget state')
        c = Checkbox('active;disabled;focus;pressed;selected;'
            'background;readonly;alternate;invalid;hover')

        # tk.Frame(App.stack[-1], width=100, height=100, borderwidth=1, relief='solid').grid()
        f = Frame()
        f.grid()
        b = Button()
        l = Label()
        e = Entry()

        App.stack.pop()
        Button()
        
        Frame()
        Button()
        Label()
        Entry()

        s = ttk.Style()

        widgets = (f, b, l, e)
        for w in widgets:
            style = w.winfo_class()
            # print(style)
            # print(s.layout(style))

        print(s.element_options('Frame.border'))
        # s.configure('TFrame', borderwidth=2, background='red', relief='raised')
        s.configure('TButton', font='Courier 24', foreground='red', padding=10)

if __name__ == '__main__':
    Demo().run()