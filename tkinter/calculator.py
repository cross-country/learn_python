from tkinter import *
root = Tk()

def check_string(str):
    if str.isdigit():
        return int(str)
    else:
        try:
            float(str)
            return float(str)
        except:
            ValueError
            return False



class Enter_block:
    def __init__(self, master):
        self.ent_1 = Entry(master,width=50)
        self.ent_2 = Entry(master, width=50)

        self.ent_1.pack()
        self.ent_2.pack()

enterbl = Enter_block(root)

class Calc_block:
    def __init__(self, master, picture, func):
        self.btn = Button(master, width=10, text=picture)
        self.btn.pack()

        self.btn['command'] = eval('self.' + func)

    def plus_func(self):
        a = enterbl.ent_1.get()
        b = enterbl.ent_2.get()

        a = check_string(a)
        b = check_string(b)
        if a == False or b == False:
            resultbl.lab['text'] = "Your input is not correct! Check it and try again."
        else:
            resultbl.lab['text'] = a + b


    def minus_func(self):
        a = enterbl.ent_1.get()
        b = enterbl.ent_2.get()

        a = check_string(a)
        b = check_string(b)
        if a == False or b == False:
            resultbl.lab['text'] = "Your input is not correct! Check it and try again."
        else:
            resultbl.lab['text'] = a - b

    def multiply_func(self):
        a = enterbl.ent_1.get()
        b = enterbl.ent_2.get()

        a = check_string(a)
        b = check_string(b)
        if a == False or b == False:
            resultbl.lab['text'] = "Your input is not correct! Check it and try again."
        else:
            resultbl.lab['text'] = a * b

    def devide_func(self):
        a = enterbl.ent_1.get()
        b = enterbl.ent_2.get()

        a = check_string(a)
        b = check_string(b)
        if a == False or b == False:
            resultbl.lab['text'] = "Your input is not correct! Check it and try again."
        else:
            resultbl.lab['text'] = a / b





class Result_block:
    def __init__(self, master):
        self.lab = Label(master, width=40, bg='black', fg='white')
        self.lab.pack()





calcbl = Calc_block(root, '+', 'plus_func')
calcbl = Calc_block(root, '-', 'minus_func')
calcbl = Calc_block(root, '*', 'multiply_func')
calcbl = Calc_block(root, '/', 'devide_func')
resultbl = Result_block(root)




root.mainloop()
