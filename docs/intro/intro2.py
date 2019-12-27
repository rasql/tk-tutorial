import tkinter as tk

class App:
    """Define the application class."""
    def __init__(self):
        self.root = tk.Tk()
        tk.Label(self.root, text='hello world!', font='Arial 24').pack()

    def run(self):
        """Run the main loop."""
        self.root.mainloop()

App().run()