from tklib import *
    
def test_label():
    label = Label()
    assert isinstance(label, Label)
    assert isinstance(label.master, tk.Tk)
    assert label['text'] == 'Label'
