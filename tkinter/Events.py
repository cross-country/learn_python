from tkinter import *

root = Tk()

def focus_in_out(event):
    if str(event.type.name) == 'FocusIn':
        event.widget['bg'] = 'white'
    elif str(event.type.name) == 'FocusOut':
        event.widget['bg'] = 'lightgrey'


def field_size(event):
    a = ent_1.get()
    b = ent_2.get()
    if a.isdigit() and b.isdigit():
        text.config(width=int(a), height=int(b))
    else:
        try:
            text.config(widht=float(a), height=float(b))
        except ValueError:
            ent_1.delete(0, END)
            ent_2.delete(0, END)
            ent_1.insert(0, 'Wrong size')






f1 = Frame()
f1.pack()

f2 = Frame(f1)
f2.pack(side=LEFT)

ent_1 = Entry(f2)
ent_1.pack()
ent_1.bind('<Return>', field_size)
ent_1.bind('<Button-3>', field_size)

ent_2 = Entry(f2)
ent_2.pack()
ent_2.bind('<Return>', field_size)
ent_2.bind('<Button-3>', field_size)

btn = Button(f1, text='Change')
btn.pack(expand=1)
btn.bind('<Button-1>', field_size)

text = Text(bg='lightgrey')
text.pack()
text.bind('<FocusIn>', focus_in_out )
text.bind('<FocusOut>', focus_in_out)




root.mainloop()