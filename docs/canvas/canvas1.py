from tklib import *
app = App('Canvas with lines and rectangles')

c = Canvas(width=600, height=300, background='lightblue')
c.create_line(10, 10, 200, 200, fill='red')
c.create_line(20, 10, 210, 200, fill='blue', width=3)
c.create_rectangle(100, 200, 150, 250, fill='green', width=2)
c.create_rectangle(300, 100, 580, 250, fill='yellow', width=5)

app.run()