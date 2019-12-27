import tkinter as tk

class App:
    """Define the application class."""
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('App Demo')
        tk.Label(self.root, text='Hello Tkinter! ' * 3).pack()

    def run(self):
        """Run the main loop."""
        self.root.mainloop()

if __name__ == '__main__':
    App().run()