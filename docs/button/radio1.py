import tkinter as tk

root = tk.Tk()
lang = tk.StringVar()
lang.set('de')

def cb():
    print(lang.get())

tk.Radiobutton(root, text='English', variable=lang, value='english', command=cb).pack()
tk.Radiobutton(root, text='German', variable=lang, value='german', command=cb).pack()
tk.Radiobutton(root, text='French', variable=lang, value='french', command=cb).pack()

root.mainloop()