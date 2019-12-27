import tkinter as tk
import tkinter.ttk as ttk

class App:
    """Define the application class."""
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('App')

        tk.Label(self.root, text='tk.Label').pack()
        ttk.Label(self.root, text='ttk.Label').pack()

        tk.Button(self.root, text='tk.Button').pack()
        ttk.Button(self.root, text='ttk.Button').pack()

    def run(self):
        """Run the main loop."""
        self.root.mainloop()

if __name__ == '__main__':
    App().run()