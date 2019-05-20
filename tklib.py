import sys, os
import tkinter as tk
import tkinter.ttk as ttk

import math
from PIL import ImageGrab

class Frame(ttk.Frame):
     def __init__(self, nb=None, **kwargs):
        if nb == None:
            super(Frame, self).__init__(App.parent, **kwargs)
        else:
            super(Frame, self).__init__(App.nb, **kwargs)
            App.nb.add(self, text=nb)
            print(App.nb, self, nb)
        # App.stack.append(App.parent)
        # App.parent = self
        self.grid()


class Label(ttk.Label):
    """Create a Label object."""
    def __init__(self, text='Label', **kwargs):
        super(Label, self).__init__(App.parent, text=text, **kwargs)
        self.grid()


class Button(ttk.Button):
    """Create a Button object."""
    def __init__(self, text='Button', cmd='', **kwargs):
        self.cmd = cmd
        super(Button, self).__init__(App.parent, text=text, command=self.cb, **kwargs)
        self.grid()

    def cb(self):
        """Evaluate the cmd string in the Button context."""
        exec(self.cmd)


class Radiobutton:
    """Create a Radiobutton object."""
    def __init__(self, items, cmd='', **kwargs):
        self.items = items.split(';')
        self.cmd = cmd
        self.v = tk.IntVar()
        self.v.set(0)
        for i, item in enumerate(items.split(';')):
            r = ttk.Radiobutton(App.parent, text=item, variable=self.v, value=i, command=self.cb, **kwargs)
            r.grid(sticky='w')

    def cb(self):
        """Evaluate the cmd string in the Radiobutton context."""
        self.item = self.items[self.v.get()]
        exec(self.cmd)

class Checkbox:
    """Create a Checkbox object."""
    def __init__(self, items, cmd='', **kwargs):
        self.items = items.split(';')
        self.v = []
        self.cmd = cmd
        for i, item in enumerate(items.split(';')):
            self.v.append(tk.IntVar())
            c = ttk.Checkbutton(App.parent, text=item, command=self.cb, variable=self.v[i], **kwargs)
            c.grid(sticky='w')

    def cb(self):
        """Evaluate the cmd string in the Checkbox context."""
        self.selection = []
        for i, item in enumerate(self.items):
            if self.v[i].get() == 1:
                self.selection.append(item)
        exec(self.cmd)

class Entry(ttk.Entry):
    """Create an Entry object with a command string."""
    def __init__(self, text, cmd='', **kwargs):
        ttk.Label(App.parent, text=text).grid()
        self.var = tk.StringVar()
        self.cmd = cmd
        super(Entry, self).__init__(App.parent, textvariable=self.var, **kwargs)
        self.bind('<Return>', self.cb)
        self.grid()

    def cb(self, event):
        """Evaluate the cmd string in the Entry context."""
        exec(self.cmd)

class Canvas(tk.Canvas):
    """Define a canvas."""
    def __init__(self, **kwargs):
        # super(Canvas, self).__init__(App.parent, width=w, height=h, bg='light blue')
        super(Canvas, self).__init__(App.parent, **kwargs)
        self.grid()

    def polygon(self, x0, y0, r, n, **kwargs):
        points = []
        for i in range(n):
            a = 2 * math.pi * i / n
            x = x0 + math.sin(a) * r
            y = y0 + math.cos(a) * r
            points.append(x)
            points.append(y)
        self.create_polygon(points, **kwargs)

class Listbox(tk.Listbox):
    """Define a Listbox object."""
    def __init__(self, items, cmd='', **kwargs):
        self.cmd = cmd
        super(Listbox, self).__init__(App.parent, **kwargs)
        if isinstance(items, str):
            items = items.split(';')
        self.items = items
        for item in items:
            self.insert(tk.END, item)
        for i in range(0, self.size(), 2):
            self.itemconfigure(i, background='#f0f0ff')
        self.grid()
        self.bind('<<ListboxSelect>>', self.cb)

    def cb(self, event):
        """Evaluate the cmd string in the Listbox context."""
        self.item = self.items[self.curselection()[0]]
        exec(self.cmd)

class Scale(tk.Scale):
    """Define a Scale object."""
    def __init__(self, **kwargs):
        self.var = tk.IntVar()
        super(Scale, self).__init__(App.parent, variable=self.var, **kwargs)
        self.grid()

class Combobox(ttk.Combobox):
    """Define a Combobox."""
    def __init__(self, values, cmd='', **kwargs):
        self.cmd = cmd
        if isinstance(values, str):
            values = values.split(';')
        self.var = tk.StringVar()
        super(Combobox, self).__init__(App.parent, textvariable=self.var, **kwargs)
        self['values'] = values
        self.bind('<<ComboboxSelected>>', self.cb)
        self.grid()

    def cb(self, event):
        """Evaluate the cmd string in the Combobox context."""
        self.item = self.var.get()
        exec(self.cmd)

class Spinbox(ttk.Spinbox):
    """Define a Spinbox widget."""
    def __init__(self, cmd='', **kwargs):
        self.cmd = cmd
        super(Spinbox, self).__init__(App.parent, **kwargs)
        self.grid()

    def cb(self, event):
        """Evaluate the cmd string in the Spinbox context."""
        exec(self.cmd)

class Separator(ttk.Separator):
    """Insert a separator line."""
    def __init__(self, **kwargs):
        super(Separator, self).__init__(App.parent, **kwargs)
        self.grid(sticky="we", pady=5)

class Labelframe(ttk.Labelframe):
    """Insert a labelframe."""
    def __init__(self, **kwargs):
        super(Labelframe, self).__init__(App.parent, **kwargs)
        App.stack.append(App.parent)
        App.parent = self
        self.grid()

class Text(tk.Text):
    """Insert a text area."""
    def __init__(self, text='', scroll='', **kwargs):
        if scroll == '':
            super(Text, self).__init__(App.parent, **kwargs)
            self.grid()
        else:
            frame = ttk.Frame(App.parent)
            frame.grid()
            super(Text, self).__init__(frame, **kwargs)
            self.grid(row=0, column=0)
            if 'x' in scroll:
                scrollx = ttk.Scrollbar(frame, orient=tk.HORIZONTAL, command=self.xview)
                scrollx.grid(row=1, column=0, sticky='we')
                self.configure(xscrollcommand=scrollx.set)
            if 'y' in scroll:
                scrolly = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.yview)
                scrolly.grid(row=0, column=1, sticky='ns')
                self.configure(yscrollcommand=scrolly.set)
        self.insert('1.0', text)

class Scrollbars:
    """Add xy scrollbars to a widget."""
    def add_scrollbars(self, Widget, scroll):
        if scroll == '':
            super(Widget, self).__init__(App.parent, **kwargs)
            self.grid()
        else:
            frame = ttk.Frame(App.parent)
            frame.grid()
            super(Widget, self).__init__(frame, **kwargs)
            self.grid(row=0, column=0)
            if 'x' in scroll:
                scrollx = ttk.Scrollbar(frame, orient=tk.HORIZONTAL, command=self.xview)
                scrollx.grid(row=1, column=0, sticky='we')
                self.configure(xscrollcommand=scrollx.set)
            if 'y' in scroll:
                scrolly = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.yview)
                scrolly.grid(row=0, column=1, sticky='ns')
                self.configure(yscrollcommand=scrolly.set)


class Canvas(tk.Canvas, Scrollbars):
    def __init__(self, **kwargs):
        self.add_scrollbars(Canvas, scroll='', **kwargs)


class Treeview(ttk.Treeview):
    """Insert a treeview area."""
    def __init__(self, items=[], **kwargs):
        super(Treeview, self).__init__(App.parent, **kwargs)
        for item in items:
            self.insert('', 'end', text=item)
        self.grid()


class Pandedwindow(ttk.Panedwindow):
    """Insert a paned window."""
    def __init__(self, **kwargs):
        super(Pandedwindow, self).__init__(App.parent, **kwargs)
        App.stack.append(self)
        App.parent = self
        self.grid()

class Notebook(ttk.Notebook):
    def __init__(self, **kwargs):
        super(Notebook, self).__init__(App.root, **kwargs)
        App.nb = self
        self.grid()

class Window():
    """Open a new window."""
    def __init__(self, title='Window'):
        top = tk.Toplevel(App.root)
        top.title(title)
        frame = ttk.Frame(top, width=200, height=200, padding=(5, 10))
        frame.pack()
        App.parent = frame
        App.stack = [root]

class App(tk.Frame):
    """Define the application base class."""
    root = tk.Tk()
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    parent = root
    stack = [parent]

    def __init__(self):
        """Define the Tk() root widget and a background frame."""
        frame = ttk.Frame(App.root, width=200, height=200, padding=(5, 10))
        frame.grid()
        App.parent = frame
        App.root.bind('<Key>', self.callback)

    def run(self):
        """Run the main loop."""
        self.root.mainloop()

    def save_img(self):
        """Save a screen capture to the current folder."""
        App.root.update()
        x = App.root.winfo_rootx()
        y = App.root.winfo_rooty()
        w = App.root.winfo_width()
        h = App.root.winfo_height()
        print(x, y, w, h)
        im = ImageGrab.grab((x, y, x+w, y+h))

        name = type(self).__name__
        module = sys.modules['__main__']
        path, name = os.path.split(module.__file__)
        name, ext = os.path.splitext(name)
        filename = path + '/' + name + '.png'
        im.save(filename)

    def callback(self, event):
        """Execute a callback function."""
        if event.char == 'p':
            self.save_img()

if __name__ == '__main__':
    App().run()