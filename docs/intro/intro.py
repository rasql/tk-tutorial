import tkinter as tk
import tkinter.ttk as ttk

class Label(ttk.Label):
    """Create a Label object."""
    def __init__(self, text='Label', **kwargs):
        super().__init__(App.stack[-1], text=text, **kwargs)
        self.grid()

class Button(ttk.Button):
    """Create a Button object."""
    def __init__(self, text='Button', **kwargs):
        super().__init__(App.stack[-1], text=text, **kwargs)
        self.grid()

class App:
    """Define the application class."""
    stack = []

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('App')
        App.stack.append(self.root)

        Label('New Label')
        Label()

        Button('New Button')
        Button()

    def run(self):
        """Run the main loop."""
        self.root.mainloop()

if __name__ == '__main__':
    App().run()