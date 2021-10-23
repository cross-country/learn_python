from tkinter import *

def add_func():
    a = ent.get()
    if a:
        list_1.insert(END, a)
        ent.delete(0, END)
    else:
        pass

def shift_left():
    select = list(list_2.curselection())
    select.reverse()
    for i in select:
        list_1.insert(END, list_2.get(i))
        list_2.delete(i)


def shift_right():
    select = list(list_1.curselection())
    select.reverse()
    for i in select:
        list_2.insert(END, list_1.get(i))
        list_1.delete(i)



root = Tk()

list_1 = Listbox(selectmode=EXTENDED)
list_1.pack(side=LEFT)

scroll_1 = Scrollbar(command=list_1.yview)
scroll_1.pack(side=LEFT)
list_1.config(yscrollcommand=scroll_1.set)

f1 = Frame()
f1.pack(side=LEFT)

ent = Entry(f1)
ent.pack(padx=2, pady=2)

btn_1 = Button(f1, text='Add', command=add_func)
btn_1.pack(padx=2, pady=2, fill=X)

btn_2 = Button(f1, text='>>>', command=shift_right)
btn_2.pack(padx=2, pady=2, fill=X)

btn_3 = Button(f1, text="<<<", command=shift_left)
btn_3.pack(padx=2, pady=2, fill=X)

list_2 = Listbox(selectmode=EXTENDED)
list_2.pack(side=LEFT)

scroll_2 = Scrollbar(command=list_2.yview)
scroll_2.pack(side=LEFT)
list_2.config(yscrollcommand=scroll_2.set)




root.mainloop()