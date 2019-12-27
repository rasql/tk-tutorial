"""Display a 2D table."""

from tklib import *
import random

n, m = 40, 10
table = []
for i in range(n):
    line = []
    for j in range(m):
        line.append(random.randint(0, 999))
    table.append(line)


class Demo(App):
    def __init__(self): 
        super().__init__()
        Label('Display a 2D table', font='Arial 24')
        Label('Click on header to sort')
        Combobox('A;B;C')
        
        tree = Treeview()
        for i in range(n):
            tree.insert('', 'end', text=table[i][0], values=table[i][1:])

        tree['columns'] = list(range(m-1))
        headings=list('ABCDEFGHI')
        for j in range(m-1):
            tree.column(j, width=50, anchor='e')
            tree.heading(j, text=headings[j])

if __name__ == '__main__':
    Demo().run()