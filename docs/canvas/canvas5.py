from tklib import *
app = App('Random circles')

w, h = 600, 300
c = Canvas(width=w, height=h, background='lightblue')

for i in range(50):
    x = random.randint(0, w)
    y = random.randint(0, h)
    r = random.randint(10, 100)
    c.create_oval(x, y, x+r, y+r)

app.run()