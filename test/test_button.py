# import the code to be tested
from tklib import *

b = Button('test')

def test_button():
    assert isinstance(b, Button)
    assert isinstance(b.master, tk.Tk)
    assert b.cmd == ''
    
def test_label():
    label = Label()
    assert isinstance(label, Label)
    assert isinstance(label.master, tk.Tk)
    assert label['text'] == 'Label'


def test_radiobutton():
    x = Radiobutton()
    assert isinstance(x, Radiobutton)
