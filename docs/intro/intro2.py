import tkinter as tk

class App:
    """Define the application class."""
    def __init__(self):

        self.root = tk.Tk()
        self.label = tk.Label(self.root, text='hello world!', font='Arial 24')
        self.label.grid()

    def run(self):
        """Run the main loop."""
        self.root.mainloop()

App().run()
