from tkinter import *
import os
from tkinter import messagebox as mb

root = Tk()
root.resizable(False, False)


def change_ext():
    directory = ent1.get()
    ext_1 = ent2.get()
    ext_2 = ent3.get()
    try:
        file_list = os.listdir(r'{}'.format(directory))
        for k in file_list:
            var1 = k.split('.')
            if os.path.isfile('{}/{}'.format(directory, k)) and var1[1] == ext_1:
                os.rename(r'{}/{}'.format(directory, k), r'{}/{}.{}'.format(directory, var1[0], ext_2))
            else:
                continue
        ent2.delete(0, END)
        ent3.delete(0, END)
    except FileNotFoundError:
        mb.showerror('Ошибка', 'Директория {} не найдена'.format(directory))
        ent2.delete(0, END)
        ent3.delete(0, END)



lab1 = Label(text='Введите полный адресс директории, в которой меняете расширения файлов: ')
lab1.grid(columnspan=3)

ent1 = Entry(width=40)
ent1.grid(columnspan=3, sticky='e', padx=3)

lab2 = Label(text='расширение_1:')
lab2.grid(row=2, column=0)

lab3 = Label(text='расширение_2:')
lab3.grid(row=2, column=2)

ent2 = Entry(width=5)
ent2.grid(row=3, column=0, sticky='e', padx=2)

ent3 = Entry(width=5)
ent3.grid(row=3, column=2, sticky='e', padx=2)

btn = Button(text='Изменить', command=change_ext)
btn.grid(row=4, column=1, pady=3)



root.mainloop()