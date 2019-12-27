from tklib import *

App()
b = Button()

att = dir(b)
print(len(att))

for a in att:
    s1 = f'b.{a}()'
    try:
        res = eval(s1)
    except:
        res = ''
    print(a, s1, res, sep='\t')

print(b.winfo_width())
print(b.winfo_x())
print(b.winfo_screenwidth())
print(b.winfo_screenheight())