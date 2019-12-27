"""Create a dir() inspector."""

from tklib import *

class Inspector(Treeview):
    """Display the configuration of a widget."""
    def __init__(self, widget):
        Window(str(widget))
        super(Inspector, self).__init__(columns=0)
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

    def select(self, event=None):
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
        
class Demo(App):
    def __init__(self): 
        super().__init__()
        Label('Inspector dir(App)', font='Arial 24')
        
        Entry('reg exp')
        Button('Refresh')

        L = dir(App)
        print(len(L))
        App.tree = Treeview(columns=(0, 1))

        for item in L:
            obj = eval('App.' + item)
            t = type(obj).__name__
            App.tree.insert('', 'end', text=item, values=(t, obj.__doc__))

        b = Button()
        b.grid()
        Inspector(b)
        Inspector(App.tree)

if __name__ == '__main__':
    Demo().run()