from tkinter import *

root = Tk()

class PhoneNumber():
    def __init__(self, block, text, value,  number):
        self.rb = Radiobutton(block, variable=var_1, width=10, indicatoron=0)
        self.rb.pack(side=TOP, padx=1, pady=2)

        self.rb['text'] = text
        self.rb['value']  =  value


        def phone():
            lab['text'] = number

        self.rb['command'] = phone





f1 = Frame()
f1.pack(side=LEFT)

var_1 = IntVar()
var_1.set(-1)

btn_1 = PhoneNumber(f1, 'Olga', 0, '0688142133')
btn_2 = PhoneNumber(f1, 'Alex', 1, '0683759031')



f2 = Frame()
f2.pack(side=LEFT, expand=1, fill=BOTH)

lab = Label(f2, width=10, bg='white')
lab.pack(expand=1, fill=BOTH)

root.mainloop()