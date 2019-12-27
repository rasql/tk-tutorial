"""Display a label with an image."""

import os
from tklib import *
from PIL import Image, ImageTk

class Demo(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Label('Show images', font='Arial 24')

        lb = Label()
        App.img0 = Image.open('icons/bell.png')
        App.img = ImageTk.PhotoImage(App.img0)
        lb['image'] = App.img

        L = 'text;image;center;top;left;bottom;right'.split(';')

        i = 0
        for l in L:
            lb = Label(l, compound=l, image=App.img, padding=10)
            lb.grid(column=i, row=1)
            i += 1

Demo().run()