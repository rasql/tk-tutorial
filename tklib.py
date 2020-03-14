import sys
import os
import re
import math
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog, colorchooser

from PIL import Image, ImageTk, ImageGrab
import random


class EntryMixin:
    """Add label, widget and callback function."""

    def add_widget(self, label, widget, kwargs):
        """Add widget with optional label."""
        if label == '':
            super(widget, self).__init__(App.stack[-1], **kwargs)
            self.grid()
        else:
            d = 2 if App.debug else 0
            frame = ttk.Frame(App.stack[-1], relief='solid', borderwidth=d)
            frame.grid(sticky='e')
            ttk.Label(frame, text=label).grid()
            super(widget, self).__init__(frame, **kwargs)
            self.grid(row=0, column=1)

    def add_cmd(self, cmd):
        # if cmd is a string store it, and replace it 'cb' callback function
        if isinstance(cmd, str):
            self.cmd = cmd
            cmd = self.cb
        self.bind('<Return>', lambda event: cmd(self, event))

    def cb(self, item=None, event=None):
        """Execute the cmd string in the widget context."""
        exec(self.cmd)


class Entry(ttk.Entry, EntryMixin):
    """Create an Entry object with label and callback."""

    def __init__(self, label='', cmd='', val='',  **kwargs):
        self.var = tk.StringVar()
        self.var.set(val)

        self.add_widget(label, Entry, kwargs)
        self['textvariable'] = self.var
        self.add_cmd(cmd)


class Combobox(ttk.Combobox, EntryMixin):
    """Create a Combobox with label and callback."""

    def __init__(self, label='', values='', cmd='', val=0, **kwargs):
        if isinstance(values, str):
            values = values.split(';')

        self.var = tk.StringVar()
        self.var.set(values[val])

        self.add_widget(label, Combobox, kwargs)
        self['textvariable'] = self.var
        self['values'] = values

        self.add_cmd(cmd)
        self.bind('<<ComboboxSelected>>', self.cb)


class Spinbox(ttk.Spinbox, EntryMixin):
    """Create a Spinbox with label and callback."""

    def __init__(self, label='', cmd='', values='', val=0, **kwargs):
        if isinstance(values, str):
            values = values.split(';')
            if len(values) > 1:
                val = values[val]

        self.var = tk.StringVar(value=val)

        self.add_widget(label, Spinbox, kwargs)
        self['textvariable'] = self.var

        if len(values) > 1:
            self['values'] = values
        self.add_cmd(cmd)


class Scale(ttk.Scale, EntryMixin):
    """Create a Spinbox with label and callback."""

    def __init__(self, label='', cmd='', val=0, **kwargs):
        self.var = tk.IntVar(value=val)

        if not 'length' in kwargs:
            kwargs.update({'length': 200})

        self.add_widget(label, Scale, kwargs)
        self['variable'] = self.var

        self.add_cmd(cmd)
        if isinstance(cmd, str):
            self.cmd = cmd
            cmd = self.cb
        self['command'] = lambda event: cmd(self, event)


class Callback:
    """Provide a callback function."""

    def cb(self, event=None):
        """Execute the cmd string in the widget context."""
        exec(self.cmd)

    def add_command(self, cmd):
        """Add the function, or execute string via callback."""
        self.cmd = cmd
        if isinstance(cmd, str):
            cmd = self.cb
        self['command'] = cmd


def Scrollable(widget, scroll='', **kwargs):
    """Add scrollbars to a widget"""
    if scroll == '':
        w = widget(App.stack[-1], **kwargs)
        w.grid()
        return w
    else:
        f = Frame()
        w = widget(App.stack[-1], **kwargs)
        w.grid()
        if 'x' in scroll:
            x = ttk.Scrollbar(App.stack[-1], orient='horizontal')
            x.grid(row=1, column=0, sticky='we')
            w.config(xscrollcommand=x.set)
            x.config(command=w.xview)
        if 'y' in scroll:
            y = ttk.Scrollbar(App.stack[-1], orient='vertical')
            y.grid(row=0, column=1, sticky='ns')
            w.config(yscrollcommand=y.set)
            y.config(command=w.yview)
        App.stack.pop()
        return w


class Frame(ttk.Frame):
    """Create a frame around widgets."""

    def __init__(self, nb=None, **kwargs):
        if nb == None:
            super(Frame, self).__init__(App.stack[-1], **kwargs)
            self.config(borderwidth=1, relief='solid')
            App.stack.append(self)
            self.grid()
        else:
            super(Frame, self).__init__(App.nb, **kwargs)
            App.nb.add(self, text=nb)
            App.stack[-1] = self


class Label(ttk.Label):
    """Create a Label object."""

    def __init__(self, text='Label', **kwargs):
        super(Label, self).__init__(App.stack[-1], text=text, **kwargs)
        self.grid()


class Button(ttk.Button):
    def __init__(self, text='Button', cmd='', **kwargs):
        self.cmd = cmd
        super().__init__(App.stack[-1], text=text, command=self.cb, **kwargs)
        self.bind('<Return>', self.cb)
        self.grid()

    def cb(self, event=None):
        if isinstance(self.cmd, str):
            exec(self.cmd)
        else:
            self.cmd()


class Radiobutton:
    """Create a list-based Radiobutton object."""

    def __init__(self, items='Radiobutton', cmd='', val=0, **kwargs):
        self.items = items.split(';')
        self.cmd = cmd
        self.val = tk.IntVar()
        self.val.set(val)
        for i, item in enumerate(self.items):
            r = ttk.Radiobutton(App.stack[-1], text=item, variable=self.val,
                                value=i, command=self.cb, **kwargs)
            r.grid(sticky='w')

    def cb(self):
        """Evaluate the cmd string in the Radiobutton context."""
        self.item = self.items[self.val.get()]
        exec(self.cmd)


class Checkbutton:
    """Create a list-based Checkbutton object."""

    def __init__(self, items='Checkbutton', cmd='', **kwargs):
        self.items = items.split(';')
        self.val = []
        self.cmd = cmd
        for i, item in enumerate(self.items):
            self.val.append(tk.IntVar())
            c = ttk.Checkbutton(
                App.stack[-1], text=item, command=self.cb, variable=self.val[i], **kwargs)
            c.grid(sticky='w')

    def cb(self):
        """Evaluate the cmd string in the Checkutton context."""
        self.selection = []
        for i, item in enumerate(self.items):
            if self.val[i].get() == 1:
                self.selection.append(item)
        exec(self.cmd)


class Canvas(tk.Canvas):
    """Define a canvas."""

    def __init__(self, **kwargs):
        # super(Canvas, self).__init__(App.stack[-1], width=w, height=h, bg='light blue')
        super(Canvas, self).__init__(App.stack[-1], **kwargs)
        self.grid()
        self.bind('<Button-1>', self.start)
        self.bind('<B1-Motion>', self.move)

    def start(self, event=None):
        # Execute a callback function.
        self.x0 = event.x
        self.y0 = event.y
        self.id = self.create_rectangle(self.x0, self.y0, self.x0, self.y0)

    def move(self, event=None):
        self.x1 = event.x
        self.y1 = event.y
        self.coords(self.id, self.x0, self.y0, self.x1, self.y1)

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

    def __init__(self, items='Listbox', cmd='', **kwargs):
        self.cmd = cmd
        super(Listbox, self).__init__(App.stack[-1], **kwargs)

        self.var = tk.StringVar()
        self.config(listvariable=self.var)
        self.set(items)
        self.coloring()
        self.obj = 'tk'

        self.grid()
        self.bind('<<ListboxSelect>>', self.cb)
        self.bind('<Button-1>', self.button1)
        self.bind('<Return>', self.enter)

    def set(self, items):
        """Set a list of items to the Listbox."""
        self.items = items
        if isinstance(items, str):
            items = items.split(';')
        self.var.set(items)

    def coloring(self):
        for i in range(self.size()):
            if i % 2:
                self.itemconfigure(i, background='#f0f0ff')
            else:
                self.itemconfigure(i, background='#ffffff')

    def cb(self, event):
        """Evaluate the cmd string in the Listbox context."""
        print('draw_selection', self.curselection())
        self.item = self.items[self.curselection()[0]]
        exec(self.cmd)

    def button1(self, event):
        print('button1', event)

    def enter(self, event):
        print('enter', event)


class ListboxSearch(Listbox):
    def __init__(self, items, **kwargs):
        Frame().grid(sticky='ns')
        self.re = Entry('regex', self.filter, width=15)
        super(ListboxSearch, self).__init__(items, **kwargs)
        self.bind('<<ListboxSelect>>', self.cb)
        App.stack.pop()

    def filter(self, event=None):
        p = self.re.val.get()
        self.delete(0, 'end')
        self.filtered = []
        for s in self.items:
            m = re.match(p, s)
            if m:
                self.insert('end', s)
        self.coloring()

    def cb(self, event):
        sel = self.curselection()[0]
        self.item = self.get(sel)
        s = self.obj + '.'+self.item+'.__doc__'
        doc = eval(s)
        App.text.delete('1.0', 'end')
        App.text.insert('end', self.item + '\n' + doc + '\n')


class Separator(ttk.Separator):
    """Insert a separator line."""

    def __init__(self, **kwargs):
        super(Separator, self).__init__(App.stack[-1], **kwargs)
        self.grid(sticky="we", pady=5)


class Labelframe(ttk.Labelframe):
    """Insert a labelframe."""

    def __init__(self, **kwargs):
        super(Labelframe, self).__init__(App.stack[-1], **kwargs)
        App.stack.append(App.stack[-1])
        App.stack[-1] = self
        self.grid()


class Text(tk.Text):
    """Insert a text area."""

    def __init__(self, text='', scroll='', **kwargs):
        if scroll == '':
            super(Text, self).__init__(App.stack[-1], **kwargs)
            self.grid()
        else:
            frame = ttk.Frame(App.stack[-1])
            frame.grid()
            super(Text, self).__init__(frame, **kwargs)
            self.grid(row=0, column=0)
            if 'x' in scroll:
                scrollx = ttk.Scrollbar(
                    frame, orient=tk.HORIZONTAL, command=self.xview)
                scrollx.grid(row=1, column=0, sticky='we')
                self.configure(xscrollcommand=scrollx.set)
            if 'y' in scroll:
                scrolly = ttk.Scrollbar(
                    frame, orient=tk.VERTICAL, command=self.yview)
                scrolly.grid(row=0, column=1, sticky='ns')
                self.configure(yscrollcommand=scrolly.set)
        self.insert('1.0', text)
        self.bind('<<Modified>>', self.on_modify)
        self.bind('<<Selection>>', self.on_select)

    def on_modify(self, event=None):
        print('modify', event)
        # flag = self.edit_modified()
        # print(flag)
        # if flag:
        #     print('changed called')
        self.edit_modified(False)

    def on_select(self, event=None):
        print('draw_selection', event)

    def set(self, text):
        """Set Text to text."""
        self.delete('1.0', 'end')
        self.insert('1.0', text)


class Scrollbars:
    """Add xy scrollbars to a widget."""

    def add_scrollbars(self, Widget, scroll, **kwargs):
        if scroll == '':
            super(Widget, self).__init__(App.stack[-1], **kwargs)
            self.grid()
        else:
            frame = ttk.Frame(App.stack[-1])
            frame.grid()
            super(Widget, self).__init__(frame, **kwargs)
            self.grid(row=0, column=0)
            if 'x' in scroll:
                scrollx = ttk.Scrollbar(
                    frame, orient=tk.HORIZONTAL, command=self.xview)
                scrollx.grid(row=1, column=0, sticky='we')
                self.configure(xscrollcommand=scrollx.set)
            if 'y' in scroll:
                scrolly = ttk.Scrollbar(
                    frame, orient=tk.VERTICAL, command=self.yview)
                scrolly.grid(row=0, column=1, sticky='ns')
                self.configure(yscrollcommand=scrolly.set)

# class Canvas(tk.Canvas, Scrollbars):
#     def __init__(self, **kwargs):
#         self.add_scrollbars(Canvas, scroll='', **kwargs)


class Treeview(ttk.Treeview):
    """Insert a treeview area."""

    def __init__(self, items=[], **kwargs):
        super(Treeview, self).__init__(App.stack[-1], **kwargs)
        for item in items:
            self.insert('', 'end', text=item)
        self.grid()
        self.bind()
        self.bind('<<TreeviewSelect>>', self.draw_selection)
        self.bind('<<TreeviewOpen>>', self.open)
        self.bind('<<TreeviewClose>>', self.close)

    def draw_selection(self, event=None):
        print('draw_selection', self.focus())
        top = self.winfo_toplevel()
        print(top, type(top))
        s = self.nametowidget('.status')
        s['text'] = 'draw_selection ' + self.focus()
        # for w in top.winfo_children():
        #     print(w)

    def open(self, event=None):
        print('open')

    def close(self, event=None):
        print('close')


class Inspector(Treeview):
    """Display the configuration of a widget."""

    def __init__(self, widget, **kwargs):
        Window(str(widget))
        super(Inspector, self).__init__(columns=0, **kwargs)
        Button('Update', 'self.update()')
        self.widget = widget
        self.update()
        self.entry = Entry('Content')
        self.entry.bind('<Return>', self.set_entry)

    def update(self):
        """Update the configuration data."""
        d = self.widget.configure()
        for k, v in d.items():
            self.insert('', 'end', text=k, values=(v[-1]))

    def draw_selection(self, event=None):
        id = self.focus()
        val = self.set(id, 0)
        self.entry.val.set(val)

    def set_entry(self, event=None):
        val = self.entry.val.get()
        id = self.focus()
        key = self.item(id)['text']
        self.set(id, 0, val)
        print(id, key, val)
        self.widget[key] = val


class Panedwindow(ttk.Panedwindow):
    """Insert a paned window."""

    def __init__(self, **kwargs):
        super(Panedwindow, self).__init__(App.stack[-1], **kwargs)
        App.stack.append(self)
        self.grid()


class Notebook(ttk.Notebook):
    def __init__(self, **kwargs):
        # super(Notebook, self).__init__(App.root, **kwargs)
        super(Notebook, self).__init__(App.stack[-1], **kwargs)
        App.nb = self
        self.grid()


class Menu(tk.Menu):
    """Add a Menu() node to which a menu Item() can be attached."""

    def __init__(self, label='Menu', id=0, **kwargs):
        super(Menu, self).__init__(App.menus[0], **kwargs)
        App.menus[id].add_cascade(menu=self, label=label)
        App.menus.append(self)


class ContextMenu(tk.Menu):
    def __init__(self, widget):
        """Create a context menu attached to a widget."""
        super(ContextMenu, self).__init__(widget)
        App.menus.append(self)

        if (App.root.tk.call('tk', 'windowingsystem') == 'aqua'):
            widget.bind('<2>', self.popup)
            widget.bind('<Control-1>', self.popup)
        else:
            widget.root.bind('<3>', self.popup)

    def popup(self, event):
        """Open a popup menu."""
        self.post(event.x_root, event.y_root)
        return 'break'


class Item(Callback):
    """Add a menu item to a Menu() node. Default is the last menu (id=-1)."""

    def __init__(self, label, cmd='', acc='', id=-1, **kwargs):
        self.cmd = cmd
        if isinstance(cmd, str):
            cmd = self.cb
        if acc != '':
            key = '<{}>'.format(acc)
            App.root.bind(key, self.cb)

        if label == '-':
            App.menus[id].add_separator()
        elif label[0] == '*':
            App.menus[id].add_checkbutton(
                label=label[1:], command=cmd, accelerator=acc, **kwargs)
        elif label[0] == '#':
            App.menus[id].add_radiobutton(
                label=label[1:], command=cmd, accelerator=acc, **kwargs)
        else:
            App.menus[id].add_command(
                label=label, command=cmd, accelerator=acc, **kwargs)


class Window:
    """Create a new root or toplevel window."""

    def __init__(self, title='Window', top=None):
        if top == None:
            top = tk.Toplevel(App.root)
        top.title(title)
        top.columnconfigure(0, weight=1)
        top.rowconfigure(0, weight=1)
        top.bind('<Command-i>', self.inspector)
        top.bind('<Command-p>', self.save_img)
        self.top = top

        frame = ttk.Frame(top, width=300, height=200, padding=(5, 10))
        frame.grid(sticky='nswe')

        App.stack.append(frame)
        App.win = top
        App.menus = [tk.Menu(App.win)]
        App.win['menu'] = App.menus[0]

    def add_statusbar(self):
        ttk.Separator(top).grid(sticky='we')
        self.status = ttk.Label(top, text='Statusbar', name='status')
        self.status.grid(sticky='we')

    def get_img(self, event=None):
        """Save a screen capture to the current folder."""
        App.root.update()
        x = self.top.winfo_rootx()
        y = self.top.winfo_rooty()
        w = self.top.winfo_width()
        h = self.top.winfo_height()
        self.img = ImageGrab.grab((x, y, x+w, y+h))
        # self.img.show()

    def save_img(self, event=None):
        self.get_img()
        name = type(self).__name__
        module = sys.modules['__main__']
        path, name = os.path.split(module.__file__)
        name, ext = os.path.splitext(name)
        filename = path + '/' + name + '.png'
        self.img.save(filename)

    def inspector(self, event=None):
        print('inspector', self)
        print()


class App(tk.Frame):
    parent = None
    stack = [None]  # current branch of the widget hierarchy: stack[-1] being last item
    menus = [None]

    """Define the application base class."""

    def __init__(self, title='Tk', debug=False):
        root = tk.Tk()
        root.option_add('*tearOff', False)

        App.debug = debug
        App.root = root
        App.stack = [root]
        App.parent = root

        menubar = tk.Menu(root)
        App.root['menu'] = menubar
        App.menus = [menubar]

        """Define the Tk() root widget and a background frame."""
        Window(top=App.root, title=title)
        self.top = root
        App.root.bind('<Key>', self.callback)
        App.root.bind('<Escape>', quit)
        App.root.createcommand('tk::mac::ShowPreferences', self.preferences)
        App.root.createcommand('tk::mac::ShowHelp', self.help)

    def run(self):
        """Run the main loop."""
        self.root.mainloop()

    def callback(self, event):
        """Execute a callback function."""
        pass

    def preferences(self):
        """Show preferences dialog."""
        print('show preferences')

    def help(self):
        """Show help menu."""
        print('show help')


if __name__ == '__main__':
    app = App('Demo app')
    Label()
    Button()
    Canvas()
    app.run()
