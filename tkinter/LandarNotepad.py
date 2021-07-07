from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd
import os

root = Tk()
root.minsize(width=500, height=400)

file_name = 'Untitled.txt'
l_text = 'Вы редактируете: {}'

def new_file():
    question = mb.askyesno('', 'Сохранить изменения в файле?')
    if question:
        save_file()
        text_field.delete(0.1, END)
    else:
        global file_name
        file_name = 'Untitled.txt'
        text_field.delete(0.1, END)
    lab1.config(text=l_text.format(os.path.basename(file_name)))

def save_file():
    if file_name == 'Untitled.txt':
        save_file_as()
    else:
        f = open(file_name, 'w')
        f.write(text_field.get(1.0, END))
        f.close()

def save_file_as():
    global file_name
    try_name = fd.asksaveasfilename(defaultextension='.txt')
    if try_name:
        file_name = try_name
        f = open(file_name, 'w')
        f.write(text_field.get(1.0, END))
        f.close()
        lab1.config(text=l_text.format(os.path.basename(file_name)))
    else:
        pass

def open_file_check():
    question = mb.askyesno('', 'Сохранить изменения в файле?')
    if question:
        save_file()
        open_file()
    else:
        open_file()


def open_file():
    global file_name
    try_name = fd.askopenfilename(
        filetypes=(('Text', '*.txt'),
                   ('ALL', '*.*'))
    )
    if try_name:
        file_name = try_name
        f = open(file_name)
        text_field.delete(0.1, END)
        text_field.insert(0.1, f.read())
        f.close()
        lab1.config(text=l_text.format(os.path.basename(file_name)))
    else:
        pass


def help_func():
    top_w = Toplevel(root)
    top_w.geometry('350x100+200+200')
    top_w.resizable(False, False)
    top_w.title('Справка ?')
    laba = Label(top_w, text='Совет:')
    laba.pack()
    lab = Label(top_w, text='Для ввода текста используйте клавиатуру')
    lab.pack()
    top_w.after(7000, lambda : top_w.destroy())



root.geometry('900x600')
root.title('LandarNotes')

lab1 = Label()
lab1.pack()
lab1.config(text=l_text.format(file_name))

main_menu = Menu(root)
root.config(menu=main_menu)

file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label='новый файл', command=new_file)
file_menu.add_command(label='открыть...', command=open_file_check)
file_menu.add_command(label='сохранить', command=save_file)
file_menu.add_command(label='сохранить как...', command=save_file_as)
file_menu.add_separator()
file_menu.add_command(label='Справка ?', command=help_func)

main_menu.add_cascade(label='Файл', menu=file_menu)

frame1 = Frame(root)
frame1.pack(expand=1, fill=BOTH)

text_field = Text(frame1, wrap=WORD)
text_field.pack(side=LEFT, expand=1, fill=BOTH, padx=6, pady=1)

RightScroll = Scrollbar(frame1, command=text_field.yview)
RightScroll.pack()
text_field.config(yscrollcommand=RightScroll.set)

lab2 = Label(text='LandarCorporation', font=('Courier', 12, 'italic'))
lab2.pack()

root.mainloop()
