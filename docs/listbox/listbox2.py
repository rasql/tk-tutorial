from tklib import *
app = App('tk attributes in Listbox')

Label("Tk attributes", font="Arial 18")
Listbox(dir(tk), height=20, cmd='App.sel["text"] = self.item')
App.sel = Label('Selection', font='Arial 18')

app.run()