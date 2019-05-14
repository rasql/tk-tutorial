import tkinter as tk
import math
from PIL import ImageGrab

class Lb:
    """Create a Label object."""
    def __init__(self, text, **kwargs):
        tk.Label(App.root, text=text, **kwargs).pack()

class Bt(tk.Button):
    """Create a Button object."""
    def __init__(self, text, command, **kwargs):
        cmd = command
        if isinstance(cmd, str):
            cmd = lambda : eval(command)
        super(Bt, self).__init__(App.root, text=text, command=cmd, **kwargs)
        self.pack()

class Rb:
    """Create a Radiobutton object."""
    def __init__(self, items, command=None, **kwargs):
        self.v = tk.IntVar()
        self.v.set(0)
        cmd = command
        if isinstance(cmd, str):
            cmd = lambda : eval(command)
        for i, item in enumerate(items.split(';')):
            r = tk.Radiobutton(App.root, text=item, command=cmd, variable=self.v, value=i, **kwargs).pack(anchor=tk.W)

class Ch:
    """Create a Checkbox object."""
    def __init__(self, items, command=None, **kwargs):
        self.v = []
        cmd = command
        if isinstance(cmd, str):
            cmd = lambda : eval(command)
        for i, item in enumerate(items.split(';')):
            v = tk.IntVar()
            self.v.append(v)
            r = tk.Checkbutton(App.root, text=item, command=cmd, variable=v, **kwargs).pack(anchor=tk.W)

class En:
    """Create an Entry object."""
    def __init__(self, text, **kwargs):
        tk.Label(App.root, text=text, **kwargs).pack()
        tk.Entry(App.root).pack()
        pass

class Can(tk.Canvas):
    """Define a canvas."""
    def __init__(self, w, h, **kwargs):
        super(Can, self).__init__(App.root, width=w, height=h, bg='light blue')
        self.pack()

    def polygon(self, x0, y0, r, n, **kwargs):
        points = []
        for i in range(n):
            a = 2 * math.pi * i / n
            x = x0 + math.sin(a) * r
            y = y0 + math.cos(a) * r
            points.append(x)
            points.append(y)
        self.create_polygon(points, **kwargs)

class Lbox(tk.Listbox):
    """Define a Listbox object."""
    def __init__(self, items, **kwargs):
        super(Lbox, self).__init__(App.root, **kwargs)
        for item in items.split(';'):
            self.insert(tk.END, item)
        self.pack()

class Sc(tk.Scale):
    """Define a Scale object."""
    def __init__(self, **kwargs):
        self.var = tk.IntVar()
        super(Sc, self).__init__(App.root, variable=self.var, **kwargs)
        self.pack(side='left')


class App(tk.Frame):
    """Define the application base class."""
    root = tk.Tk()

    def __init__(self):
        # Lb('Hello Tkinter!')
        Sc()
        Sc()
        Sc()

    def run(self):
        self.root.mainloop()

    def save_img(self):
        App.root.update()
        x = App.root.winfo_rootx()
        y = App.root.winfo_rooty()
        w = App.root.winfo_width()
        h = App.root.winfo_height()
        print(x, y, w, h)
        im = ImageGrab.grab((x, y, x+w, y+h))
        im.save('test.png')
        im.show()

if __name__ == '__main__':
    App().run()