import tkinter as tk
import tkinter.ttk as ttk

class App:
    """Define the application class."""
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('App Demo')
        tk.Label(self.root, text='Placing multiple widgets').pack()

        tk.Label(self.root, text='Label').pack()
        ttk.Label(self.root, text='Label').pack()

        tk.Button(self.root, text='Button').pack()
        ttk.Button(self.root, text='Button').pack()

        tk.Radiobutton(self.root, text='Radiobutton').pack()
        ttk.Radiobutton(self.root, text='Radiobutton').pack()

        tk.Checkbutton(self.root, text='Checkbutton').pack()
        ttk.Checkbutton(self.root, text='Checkbutton').pack()

    def run(self):
        """Run the main loop."""
        self.root.mainloop()

if __name__ == '__main__':
    App().run()