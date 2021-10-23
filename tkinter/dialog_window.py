from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd

root = Tk()

def open_doc():
    file_name = fd.askopenfilename(
        filetypes=(("Text", "*.txt"),
                   ("HTML", "*.html;*.htm"),
                   ("ALL", "*.*"))
    )
    if file_name:
        f = open(file_name)
        g = f.read()
        text.delete(1.0, END)
        text.insert(1.0, g)
        f.close()
    else:
        mb.showwarning("Warning!", "The file is not open")

def save_doc():
    file_name = fd.asksaveasfilename(defaultextension='txt',
        filetypes=(("Text", "*.txt"),
                   ("HTML", "*.html;*.htm"),
                   ("ALL", "*.*"))
    )
    if file_name:
        f = open(file_name, 'w')
        g = text.get(0.1, END)
        f.write(g)
        f.close()
    else:
        mb.showwarning('Be aware!', 'Your file is not saved')


def del_text():
    ask = mb.askyesno('Delete', 'Do you really want to delete the text?')
    if ask:
        text.delete(0.1, END)

    else:
        pass




text = Text(width=50, height=25)
text.grid(columnspan=2)

btn1 = Button(text='open', command=open_doc)
btn1.grid(row=1, column=0, sticky=E)
#btn1.bind('<Button-1>', open_doc)

btn2 = Button(text='save', command=save_doc)
btn2.grid(row=1, column=1, sticky=W)
#btn2.bind('<Button-1>', save_doc)

btn3 = Button(text='Delete text', command=del_text)
btn3.grid(row=1, column=1, sticky=E)


root.mainloop()
