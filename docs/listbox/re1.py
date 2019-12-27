"""Regular expression demo."""
from tkinter import *
from tklib import *
import re

class Browser(Listbox):
    def cb(self, event):
        pass

class Demo(App):
    def __init__(self): 
        super().__init__()
        Label('Regular expressions', font='Arial 18')
        Label('Enter a Perl-style regular expression')
        App.re = Entry('regex')
        App.re.bind('<Key>', self.recompile)
        App.status = Label('Status')

        Checkbox('IGNORECASE;MULITILINE;DOTALL;VERBOSE')

        Label('Enter a string to search')
        Radiobutton('Highlight first;Highligth all')
        
        App.str = Text(height=10)
        App.str.bind('<Key>', self.reevaluate)
        App.str.tag_configure("hit", background="yellow")

        Label('Groups')
        App.groups = Listbox()

        btags = App.re.bindtags()
        App.re.bindtags(btags[1:] + btags[:1])

        btags = App.str.bindtags()
        App.str.bindtags(btags[1:] + btags[:1])
        self.compiled = None

    def recompile(self, event=None):
        print('recompile')
        try:
            self.compiled = re.compile(App.re.get())
        except re.error as msg:
            self.compiled = None
            App.status.config(
                    text="re.error: %s" % str(msg),
                    background="red")
        self.reevaluate()

    def reevaluate(self, event=None):
        print('reevaluate')
        try:
            self.str.tag_remove("hit", "1.0", END)
        except TclError:
            pass
        try:
            self.str.tag_remove("hit0", "1.0", END)
        except TclError:
            pass
        self.groups.delete(0, END)
        if not self.compiled:
            return
        self.str.tag_configure("hit", background="yellow")
        self.str.tag_configure("hit0", background="orange")
        text = self.str.get("1.0", END)
        last = 0

        nmatches = 0
        while last <= len(text):
            m = self.compiled.search(text, last)
            if m is None:
                break
            first, last = m.span()
            if last == first:
                last = first+1
                tag = "hit0"
            else:
                tag = "hit"
            pfirst = "1.0 + %d chars" % first
            plast = "1.0 + %d chars" % last
            self.str.tag_add(tag, pfirst, plast)
            if nmatches == 0:
                self.str.yview_pickplace(pfirst)
                groups = list(m.groups())
                groups.insert(0, m.group())
                for i in range(len(groups)):
                    g = "%2d: %r" % (i, groups[i])
                    App.groups.insert(END, g)
            nmatches = nmatches + 1
            if self.showvar.get() == "first":
                break

        if nmatches == 0:
            self.status.config(text="(no match)",
                                      background="yellow")
        else:
            self.status.config(text="")

Demo().run()