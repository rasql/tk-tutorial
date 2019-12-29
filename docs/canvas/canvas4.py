from tklib import *
app = App('Draw a polygon')

c = Canvas(width=600, height=300, background='lightblue')
c.polygon(150, 150, 100, 6, fill='blue')
c.polygon(450, 150, 80, 8, fill='red', width=5)

app.run()