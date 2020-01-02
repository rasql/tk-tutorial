# Entry widget for Entry, Combobox, Spinbox and Scale
from tklib import *

def cb(caller, event):
    """Callback function."""
    print('item =', item)
    print('value =', item.var.get())
    print('event =', event)

class EntryMixin:
    """Add callback function."""

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

        if label == '':
            super().__init__(App.stack[-1], textvariable=self.var, **kwargs)
            self.grid()
        else:
            frame = ttk.Frame(App.stack[-1], relief='solid', borderwidth=2)
            frame.grid(sticky='e')
            ttk.Label(frame, text=label).grid()
            super().__init__(frame, textvariable=self.var, **kwargs)
            self.grid(row=0, column=1)

        self.add_cmd(cmd)


class Combobox(ttk.Combobox, EntryMixin):
    """Create a Combobox with label and callback."""

    def __init__(self, label='', values='', cmd='', val=0, **kwargs):

        if isinstance(values, str):
            values = values.split(';')
        self.var = tk.StringVar()
        self.var.set(values[val])

        if label == '':
            super().__init__(
                App.stack[-1], textvariable=self.var, values=values, **kwargs)
            self.grid()
        else:
            frame = ttk.Frame(App.stack[-1], relief='solid', borderwidth=2)
            frame.grid(sticky='e')
            ttk.Label(frame, text=label).grid()
            super().__init__(frame, textvariable=self.var, values=values, **kwargs)
            self.grid(row=0, column=1)

        self.add_cmd(cmd)
        self.bind('<<ComboboxSelected>>', self.cb)


class Spinbox(ttk.Spinbox, EntryMixin):
    """Create a Spinbox with label and callback."""

    def __init__(self, label='', cmd='', val=0, **kwargs):

        self.var = tk.StringVar(value=val)

        if label == '':
            super().__init__(
                App.stack[-1], textvariable=self.var, **kwargs)
            self.grid()
        else:
            frame = ttk.Frame(App.stack[-1], relief='solid', borderwidth=2)
            frame.grid(sticky='e')
            ttk.Label(frame, text=label).grid()
            super().__init__(frame, textvariable=self.var, **kwargs)
            self.grid(row=0, column=1)

        self.add_cmd(cmd)


class Scale(ttk.Scale, EntryMixin):
    """Create a Spinbox with label and callback."""

    def __init__(self, label='', cmd='', val=0, **kwargs):

        self.var = tk.IntVar(value=val)

        if label == '':
            super().__init__(
                App.stack[-1], variable=self.var, **kwargs)
            self.grid()
        else:
            frame = ttk.Frame(App.stack[-1], relief='solid', borderwidth=2)
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
    app = App('Entry widgets')
    Entry('Call cb', cb)
    Entry('Name', 'print(self.var.get())')
    Entry('', 'print(self.var.get())', val='inital value')
    Entry('Password', 'print(self.var.get())', show='*')
    Entry('', 'print(self.var.get())', show='*', val='inital')
    Combobox('Language', 'French;German;English', 'print(self.var.get())')
    Combobox('', 'French;German;English', 'print(self.var.get())', val=2)
    Spinbox('Label', to=10, )
    Spinbox('Label', 'print(self.var.get())', to=10, width=10)
    Scale('Scale', 'print(self.var.get())', to=10)
    Scale(cmd='print(self.var.get())', to=100)
    app.run()
