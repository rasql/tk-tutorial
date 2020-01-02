from tklib import *
app = App('Combobox')

Label('Combobox with text entry')
days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
day = tk.StringVar()
day.set(days[0])
ttk.Combobox(App.stack[-1], textvariable=day, values=days).grid()

Label('state=readonly')
day2 = tk.StringVar()
day2.set(days[1])
ttk.Combobox(App.stack[-1], textvariable=day2, values=days, state='readonly').grid()

app.run()