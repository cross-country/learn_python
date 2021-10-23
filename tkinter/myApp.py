from tkinter import *
from tkinter import messagebox

root = Tk()

def btn_click():
    login = loginInput.get()
    password = passField.get()

    info_str = f"Данные: {str(login)}, {str(password)}"
    messagebox.showinfo(title="название", message=info_str)

    # окно с ошибкой
    # messagebox.showerror(title="", message="Error always!!!!")



root["bg"] = "#fafafa"
root.title("Мое приложение")
root.wm_attributes("-alpha", 1.0)
root.geometry("600x400")

root.resizable(width=False, height=False)

canvas = Canvas(root, height=600, width=400)
canvas.pack()

frame = Frame(root, bg="red")
frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)

title = Label(frame, text="подсказка", bg="gray", font="40")
title.pack()
btn = Button(frame, text="кнопка", bg="yellow", command=btn_click)
btn.pack()

loginInput = Entry(frame, bg="white")
loginInput.pack()

passField = Entry(frame, bg="white", show="*")
passField.pack()


root.mainloop()

