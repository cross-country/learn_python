from tkinter import *

root =Tk()

red = ['red', '#ff0000']
orange = ['orange', '#ff7d00']
yellow = ['yellow', '#ffff00']
green = ['green', '#00ff00']
lightblue = ['lightblue', '#007dff']
blue = ['blue', '#0000ff']
violette = ['violette', '#7d00ff']




class Block:
    def __init__(self, master):
        self.lab = Label(master, width=25)
        self.ent = Entry(master, width=25)

        self.lab.pack()
        self.ent.pack()


class Button_Block:
    def __init__(self, master, colour, func):
        self.btn = Button(master, width=25, bg=colour[1])
        self.my_colour = colour

        self.btn['command'] = eval('self.' + func)
        self.btn.pack()

    def my_func(self):
        head.ent.delete(0, END)
        head.ent.insert(0, self.my_colour[1])
        head.lab['text'] = self.my_colour[0]





head = Block(root)
my_button = Button_Block(root, red, 'my_func')
my_button = Button_Block(root, orange, 'my_func')
my_button = Button_Block(root, yellow, 'my_func')
my_button = Button_Block(root, green, 'my_func')
my_button = Button_Block(root, lightblue, 'my_func')
my_button = Button_Block(root, blue, 'my_func')
my_button = Button_Block(root, violette, 'my_func')


root.mainloop()