import tkinter as tk

class Lb:
    """Create a Label object."""
    def __init__(self, text, **kwargs):
        tk.Label(App.root, text=text, **kwargs).pack()

class Bt:
    """Create a Button object."""
    def __init__(self, text, command, **kwargs):
        cmd = command
        if isinstance(cmd, str):
            cmd = lambda : eval(command)
        tk.Button(App.root, text=text, command=cmd, **kwargs).pack()

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

class App(tk.Frame):
    """Define the application base class."""
    root = tk.Tk()

    def __init__(self):
        Lb('Hello Tkinter!')

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    App().run()