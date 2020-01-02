import tkinter as tk

root = tk.Tk()

texts = ['English', 'German', 'French']
vars = [tk.StringVar(value='0'), tk.StringVar(value='0'), tk.StringVar(value='0')]

def cb():
    print('--- languages ---')
    for i, s in enumerate(texts):
        print(s, vars[i].get())

tk.Checkbutton(root, text=texts[0], variable=vars[0], command=cb).pack()
tk.Checkbutton(root, text=texts[1], variable=vars[1], command=cb).pack()
tk.Checkbutton(root, text=texts[2], variable=vars[2], command=cb).pack()

root.mainloop()