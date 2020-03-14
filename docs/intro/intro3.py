import tkinter as tk
import tkinter.ttk as ttk

class App:
    """Define the application class."""
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('App')

        tk.Label(self.root, text='old classic tk.Label').grid()
        ttk.Label(self.root, text='new themed ttk.Label').grid()

        tk.Button(self.root, text='tk.Button').grid()
        ttk.Button(self.root, text='ttk.Button').grid()

    def run(self):
        """Run the main loop."""
        self.root.mainloop()

App().run()