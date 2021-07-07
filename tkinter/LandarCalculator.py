#!/usr/bin/env python3
import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.title('LandarCalculator')
root.geometry()
root.resizable(False, False)
root.configure(bg='#F0F8FF')

def lab_big_len():
    ln = len(lab_big['text'])
    if ln < 17:
        style.configure('S.TLabel', font='Arial 34 bold')
    elif 29 > ln > 17:
        style.configure('S.TLabel', font='Arial 20 bold')
    elif 35 > ln > 29:
       style.configure('S.TLabel', font='Arial 16 bold')
    elif ln > 35:
        BackSpace_2()

def lab_big_len_2():
    ln = len(lab_big['text'])
    if ln < 17:
        style.configure('S.TLabel', font='Arial 34 bold')
    elif 29 > ln > 17:
        style.configure('S.TLabel', font='Arial 20 bold')
    elif 35 > ln > 29:
       style.configure('S.TLabel', font='Arial 16 bold')

def clear_lab(event):
    lab_big['text'] = '0'
    lab_little['text'] = ''
    lab_big_len()

def BackSpace(event):
    my_list = list(lab_big['text'])
    my_list.pop()
    lab_big['text'] = ''.join(my_list)
    if len(lab_big['text']) < 1:
        lab_big['text'] = '0'
    lab_big_len()

def BackSpace_2():
    my_list = list(lab_big['text'])
    my_list.pop()
    lab_big['text'] = ''.join(my_list)
    if len(lab_big['text']) < 1:
        lab_big['text'] = '0'

def decimal_key(event):
    my_list = lab_big['text'].split('.')
    if len(my_list) > 1:
        pass
    else:
        lab_big['text'] += '.'

def get_button(event):
    symb = event.keysym.split('_')
    lab_big_list = list(lab_big['text'])
    if len(lab_big_list) > 1:
        if lab_big_list[0] == '0' and lab_big_list[1] != '.':
            lab_big_list.pop(0)
            lab_big['text'] = lab_big['text'].join(lab_big_list)
        elif lab_big['text'] == 'inf':
            lab_big['text'] = '0'
    else:
        if lab_big_list[0] == '0':
            lab_big_list.pop(0)
            lab_big['text'] = lab_big['text'].join(lab_big_list)
    lab_big['text'] += symb[1]
    lab_big_len()

def get_button_2(event):
    symb = event.widget['text']
    lab_big_list = list(lab_big['text'])
    if len(lab_big_list) > 1:
        if lab_big_list[0] == '0' and lab_big_list[1] != '.':
            lab_big_list.pop(0)
            lab_big['text'] = lab_big['text'].join(lab_big_list)
        elif lab_big['text'] == 'inf':
            lab_big['text'] = '0'
    else:
        if lab_big_list[0] == '0':
            lab_big_list.pop(0)
            lab_big['text'] = lab_big['text'].join(lab_big_list)
    lab_big['text'] += symb
    lab_big_len()

def define_sign():
    global sign
    global sign_str
    if sign == 'KP_Multiply':
        sign_str = 'x'
    elif sign == 'KP_Divide':
        sign_str = '/'
    elif sign == 'KP_Add':
        sign_str = '+'
    elif sign == 'KP_Subtract':
        sign_str = '-'
    else:
        sign_str = '?'

def count(key, par1, par2):
    if key == 'x':
        return par1 * par2
    elif key == '/':
        try:
            return par1 / par2
        except ZeroDivisionError:
            return 0
    elif key == '+':
        return par1 + par2
    elif key == '-':
        return par1 - par2

def calculate(event):
    global sign
    global sign_str
    global var1_list
    sign_str = ''
    sign = event.keysym
    var1 = lab_little['text']
    var2 = lab_big['text']
    var1_list = var1.split()
    define_sign()
    if var1 == '':
        var1 = var2 + ' ' + sign_str
    elif len(var1_list) > 1:
        var1 = count(var1_list[1], float(var1_list[0]), float(var2))
        var1 = str(var1) + ' ' + sign_str
    else:
        print('something wrong')
    lab_little['text'] = var1
    lab_big['text'] = '0'

def calculate_2(event):
    sign_str = event.widget['text']
    var1 = lab_little['text']
    var2 = lab_big['text']
    var1_list = var1.split()
    if var1 == '':
        var1 = var2 + ' ' + sign_str
    elif len(var1_list) > 1:
        var1 = count(var1_list[1], float(var1_list[0]), float(var2))
        var1 = str(var1) + ' ' + sign_str
    else:
        print('something wrong')
    lab_little['text'] = var1
    lab_big['text'] = '0'

def enter_func(event):
    global var1_list
    var1 = lab_little['text']
    var2 = lab_big['text']
    var1_list = var1.split()
    if var1 == '':
        var1 = var2
    elif len(var1_list) > 1:
        var1 = count(var1_list[1], float(var1_list[0]), float(var2))
        var1 = str(var1)
    else:
        print('something wrong')
    lab_little['text'] = ''
    lab_big['text'] = var1
    lab_big_len_2()

root.bind('<KeyPress-KP_0>', get_button)
root.bind('<KeyPress-KP_1>', get_button)
root.bind('<KeyPress-KP_2>', get_button)
root.bind('<KeyPress-KP_3>', get_button)
root.bind('<KeyPress-KP_4>', get_button)
root.bind('<KeyPress-KP_5>', get_button)
root.bind('<KeyPress-KP_6>', get_button)
root.bind('<KeyPress-KP_7>', get_button)
root.bind('<KeyPress-KP_8>', get_button)
root.bind('<KeyPress-KP_9>', get_button)
root.bind('<KeyPress-KP_Decimal>', decimal_key)
root.bind('<KeyPress-KP_Add>', calculate)
root.bind('<KeyPress-KP_Subtract>', calculate)
root.bind('<KeyPress-KP_Multiply>', calculate)
root.bind('<KeyPress-KP_Divide>', calculate)
root.bind('<KeyPress-KP_Enter>', enter_func)
root.bind('<KeyPress-BackSpace>', BackSpace)

root.grid_rowconfigure(0, minsize=50)
root.grid_rowconfigure(1, minsize=150)

style = ttk.Style()

style.configure('TButton', width=6, font='Arial 20', borderwidth=2, background='#F5F5F5')
style.configure('TLabel', width=14, background='#F0F8FF', anchor='e', font='Arial 16')
style.configure('S.TLabel', font='Arial 34 bold')

lab_little = ttk.Label(root, text='')
lab_little.grid(row=0, column=0, columnspan=4, sticky='w'+'e')

lab_big = ttk.Label(root, text='0', style='S.TLabel')
lab_big.grid(row=1, column=0, columnspan=4, sticky='n'+'s'+'w'+'e')


btn1 = ttk.Button(text='1')
btn1.grid(row=6, column=0, padx=4, pady=4, ipady=20)

btn2 = ttk.Button(text='2')
btn2.grid(row=6, column=1, padx=4, pady=4, ipady=20)

btn3 = ttk.Button(text='3')
btn3.grid(row=6, column=2, padx=4, pady=4, ipady=20)

btn4 = ttk.Button(text='4')
btn4.grid(row=5, column=0, padx=4, pady=4, ipady=20)

btn5 = ttk.Button(text='5')
btn5.grid(row=5, column=1, padx=4, pady=4, ipady=20)

btn6 = ttk.Button(text='6')
btn6.grid(row=5, column=2, padx=4, pady=4, ipady=20)

btn7 = ttk.Button(text='7')
btn7.grid(row=4, column=0, padx=4, pady=4, ipady=20)

btn8 = ttk.Button(text='8')
btn8.grid(row=4, column=1, padx=4, pady=4, ipady=20)

btn9 = ttk.Button(text='9')
btn9.grid(row=4, column=2, padx=4, pady=4, ipady=20)

btn0 = ttk.Button(text='0')
btn0.grid(row=7, column=0, columnspan=2, sticky='w'+'e', padx=4, pady=4, ipady=20)

btn_minus = ttk.Button(text='-')
btn_minus.grid(row=4, column=3, padx=4, pady=4, ipady=20)

btn_plus = ttk.Button(text='+')
btn_plus.grid(row=5, column=3, rowspan=2, sticky='n'+'s', padx=4, pady=4, ipady=20)

btn_mult = ttk.Button(text='x')
btn_mult.grid(row=3, column=2, padx=4, pady=4, ipady=20)

btn_backspace = ttk.Button(text='<bsp')
btn_backspace.grid(row=3, column=3, padx=4, pady=4, ipady=20)

btn_divide = ttk.Button(text='/')
btn_divide.grid(row=3, column=1, padx=4, pady=4, ipady=20)

btn_eql = ttk.Button(text='=')
btn_eql.grid(row=7, column=3, sticky='n'+'s', padx=4, pady=4, ipady=20)

btn_clear = ttk.Button(text='C')
btn_clear.grid(row=3, column=0, padx=4, pady=4, ipady=20)

btn_point = ttk.Button(text='.')
btn_point.grid(row=7, column=2, padx=4, pady=4, ipady=20)

btn_clear.bind('<Button-1>', clear_lab)
btn_point.bind('<Button-1>', decimal_key)
btn_backspace.bind('<Button-1>', BackSpace)
btn_eql.bind('<Button-1>', enter_func)
btn1.bind('<Button-1>', get_button_2)
btn2.bind('<Button-1>', get_button_2)
btn3.bind('<Button-1>', get_button_2)
btn4.bind('<Button-1>', get_button_2)
btn5.bind('<Button-1>', get_button_2)
btn6.bind('<Button-1>', get_button_2)
btn7.bind('<Button-1>', get_button_2)
btn8.bind('<Button-1>', get_button_2)
btn9.bind('<Button-1>', get_button_2)
btn0.bind('<Button-1>', get_button_2)
btn_plus.bind('<Button-1>', calculate_2)
btn_minus.bind('<Button-1>', calculate_2)
btn_mult.bind('<Button-1>', calculate_2)
btn_divide.bind('<Button-1>', calculate_2)

root.mainloop()