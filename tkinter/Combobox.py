from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.geometry('250x200')

def change_color(event):
    can.config(background=combo.get())

combo = ttk.Combobox(root, values=['white', 'green', 'red', 'yellow', 'black'])
combo.pack()
combo.current(1)
combo.configure(state='readonly')
combo.bind('<<ComboboxSelected>>', change_color)

can = Canvas(background=combo.get())
can.pack()

print()

root.mainloop()