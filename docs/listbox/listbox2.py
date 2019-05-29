"""Display tk attributes in a listbox."""

from tklib import *

class Demo(App):
    def __init__(self): 
        super(Demo, self).__init__()

        Label("Tk attributes", font="Arial 18")
        Listbox(dir(tk), height=20, cmd='App.sel["text"] = self.item')

        App.sel = Label('Selection', font='Arial 24')

        Listbox('Mon;Tue;Wed;Thu;Fri;Sat;Sun', 'print(self)')

        Label("Listbox multiple", font="Arial 18")
        Listbox('Mon;Tue;Wed;Thu;Fri;Sat;Sun', selectmode=tk.MULTIPLE)

        Label("Listbox extended", font="Arial 18")
        Listbox('Mon;Tue;Wed;Thu;Fri;Sat;Sun', selectmode=tk.EXTENDED)

if __name__ == '__main__':
    Demo().run()