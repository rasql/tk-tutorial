import tkinter as tk

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.w = tk.Label(self.root, text='Hello Tkinter!').pack()

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    App().run()