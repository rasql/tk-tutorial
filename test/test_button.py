from tklib import *

b = Button('test')

def test_button():
    assert isinstance(b, Button)
    assert isinstance(b.master, kt.Tk)
    assert b.cmd == ''
    
