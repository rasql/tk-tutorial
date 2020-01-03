# Entry widget for Entry, Combobox, Spinbox and Scale
from tklib import *


def cb(caller, event):
    """Callback function."""
    print('caller =', caller)
    print('value =', caller.var.get())
    print('event =', event)


class EntryMixin:
    """Add callback function."""

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

        """The arguments are differnt for Entry, Combobox, Spinbox, Slider.
        Without label, grid() should have no arguments."""

        # if label == '':
        #     super().__init__(App.stack[-1], textvariable=self.var, **kwargs)
        #     self.grid()
        # else:
        #     d = 2 if App.debug else 0
        #     frame = ttk.Frame(App.stack[-1], relief='solid', borderwidth=d)
        #     frame.grid(sticky='e')
        #     ttk.Label(frame, text=label).grid()
        #     super(Entry, self).__init__(frame, textvariable=self.var, **kwargs)
        #     self.grid(row=0, column=1)

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

        # if label == '':
        #     super().__init__(
        #         App.stack[-1], textvariable=self.var, values=values, **kwargs)
        #     self.grid()
        # else:
        #     d = 2 if App.debug else 0
        #     frame = ttk.Frame(App.stack[-1], relief='solid', borderwidth=d)
        #     frame.grid(sticky='e')
        #     ttk.Label(frame, text=label).grid()
        #     super().__init__(frame, textvariable=self.var, values=values, **kwargs)
        #     self.grid(row=0, column=1)

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

        if label == '':
            super().__init__(
                App.stack[-1], textvariable=self.var, values=values, **kwargs)
            self.grid()
        else:
            d = 2 if App.debug else 0
            frame = ttk.Frame(App.stack[-1], relief='solid', borderwidth=d)
            frame.grid(sticky='e')
            ttk.Label(frame, text=label).grid()
            super().__init__(frame, textvariable=self.var, values=values, **kwargs)
            self.grid(row=0, column=1)

        self.add_cmd(cmd)


class Scale(ttk.Scale, EntryMixin):
    """Create a Spinbox with label and callback."""

    def __init__(self, label='', cmd='', val=0, **kwargs):

        self.var = tk.IntVar(value=val)

        if not 'length' in kwargs:
            kwargs.update({'length': 200})

        if label == '':
            super().__init__(
                App.stack[-1], variable=self.var, **kwargs)
            self.grid()
        else:
            d = 2 if App.debug else 0
            frame = ttk.Frame(App.stack[-1], relief='solid', borderwidth=d)
            frame.grid(sticky='e')
            ttk.Label(frame, text=label).grid()
            super().__init__(frame, variable=self.var, **kwargs)
            self.grid(row=0, column=1)

        self.add_cmd(cmd)
        if isinstance(cmd, str):
            self.cmd = cmd
            cmd = self.cb
        self['command'] = lambda event: cmd(self, event)


if __name__ == '__main__':
    app = App('Entry widgets', True)

    Entry('Entry', 'print(self.var.get())')
    Entry('', 'print(self.var.get())', val='inital value', width=10)
    Combobox('Combobox', 'Item 1;Item 2;Item 3', 'print(self.var.get())')
    Combobox('', 'Item 1;Item 2;Item 3',
             'print(self.var.get())', val=2, width=10)
    Spinbox('Spinbox', to=10, val=5)
    Spinbox('', 'print(self.var.get())', to=10, width=10)
    Scale('Scale', 'print(self.var.get())', to=10, val=5)
    Scale(cmd='print(self.var.get())', to=100, length=100)

    app.run()
