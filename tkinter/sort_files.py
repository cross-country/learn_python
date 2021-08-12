import tkinter as tk
import tkinter.ttk as ttk
import os
import shutil
from tkinter import messagebox as mb

window = tk.Tk()
window.geometry('650x350')
window.resizable(False, False)
window.title('Sort It Now')
window.configure(background='#bcc6cc')


def return_extension():
    ext_str = ent_ext.get()
    ext2_str = ''
    for i in ext_str:
        if i != ' ':
            ext2_str += i
        else:
            continue
    return ext2_str.split(';')

def one_folder_sort(path):
    directory = path
    ext_list = return_extension()
    name = directory + os.sep + os.path.basename(directory) + '_' + ent_pattern.get()
    if os.path.exists(directory):
        list_dir = os.listdir(directory)
        if os.path.exists(name):
            name = name + "333"
            os.mkdir(name)
        else:
            os.mkdir(name)

        for k in list_dir:
            my_path = '{}{}{}'.format(directory, os.sep, k)
            if os.path.isfile(my_path):
                extension = os.path.splitext(k)
                for i in ext_list:
                    if r'{}{}'.format(os.extsep, i) == extension[1]:
                        shutil.copy(my_path, name)
                        os.remove(my_path)
    else:
        mb.showerror('Ошибка!', 'Не могу найти указанный путь!')



def subfolders_sort(path):
    directory = path
    ext_list = return_extension()
    name = directory + os.sep + os.path.basename(directory) + '_' + ent_pattern.get()
    if os.path.exists(directory):
        list_dir = os.listdir(directory)
        if os.path.exists(name):
            name = name + "333"
            os.mkdir(name)
        else:
            os.mkdir(name)

        for k in list_dir:
            my_path = '{}{}{}'.format(directory, os.sep, k)
            if os.path.isfile(my_path):
                extension = os.path.splitext(k)
                for i in ext_list:
                    if r'{}{}'.format(os.extsep, i) == extension[1]:
                        shutil.copy(my_path, name)
                        os.remove(my_path)
            elif os.path.isdir(my_path):
                subfolders_sort(my_path)
    else:
        mb.showerror('Ошибка!', 'Не могу найти указанный путь!')



def start_sorting(event):
    if check_var.get() == False:
        one_folder_sort(ent_dir.get())
    elif check_var.get() == True:
        subfolders_sort(ent_dir.get())
    else:
        print('Something is wrong with checkbutton!')




check_var = tk.BooleanVar()
check_var.set(False)

lab_main = ttk.Label(window, style='main.TLabel',
                     text='Сортировать файлы по их расширениям \n (файлы будут помещены в отдельную паку).')
lab1 = ttk.Label(window, text='Укажите полный путь к папке: ')
ent_dir = ttk.Entry(window)
check_btn = tk.Checkbutton(window, variable=check_var, onvalue=True, offvalue=False,
                           text='Применить сортировку для всех вложенных папок')
lab2 = ttk.Label(window, text='Введите расширение файлов через " ; " ')
ent_ext = ttk.Entry(window, justify='center')
lab3 = ttk.Label(window, text='Имя папки будет состоять из: ')
lab4 = ttk.Label(window, text=' "названия текущего каталога"   и ')
ent_pattern = ttk.Entry(window, justify='center')
btn_sort = ttk.Button(window, text='Сортировать')
btn_sort.bind('<Button-1>', start_sorting)

lab_main.place(relx=0, rely=0, relwidth=1)
lab1.place(relx=0.02, rely=0.2)
ent_dir.place(relx=0.05, rely=0.3, relwidth=0.9)
check_btn.place(relx=0.02, rely=0.4)
lab2.place(relx=0.02, rely=0.6)
ent_ext.place(relx=0.53, rely=0.6, relwidth=0.25)
lab3.place(relx=0.02, rely=0.8)
lab4.place(relx=0.02, rely=0.9)
ent_pattern.place(relx=0.45, rely=0.9, relwidth=0.3)
btn_sort.place(relx=0.8, rely=0.9)

ent_pattern.insert(0, 'ваш вариант')
ent_ext.insert(0, 'txt;pdf')

style = ttk.Style()
style.configure('main.TLabel', background='#98afc7', anchor=tk.CENTER, font='Helvetica 14 bold')
style.configure('TLabel', font=('Helvetica', '12', 'bold'), background='#bcc6cc')
style.configure('TButton', background='#a0cfec')
style.configure('TEntry')





window.mainloop()