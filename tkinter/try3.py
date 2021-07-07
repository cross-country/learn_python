import tkinter as tk
import tkinter.ttk as ttk

window = tk.Tk()

ent = tk.Entry(justify=tk.CENTER)
#ent.place(relx=0, rely=0)
ent.pack()

#style = ttk.Style()
#style.configure('TEntry', justify='')



window.mainloop()