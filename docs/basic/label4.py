"""Display images as listbox."""
from tklib import *
from PIL import Image, ImageTk

class Demo(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Label('Show images in a treeview', font='Arial 24')

        dir = os.listdir('icons')
        self.tree = Treeview(height=20)
        self.images = []
        for file in dir:
            path = 'icons/' + file
            img0 = Image.open(path)
            img = ImageTk.PhotoImage(img0)
            self.images.append(img)
            self.tree.insert('', 'end', text=file, image=img)

Demo().run()