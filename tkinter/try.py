import tkinter as tk
import tkinter.ttk as ttk

window =tk.Tk()

ent1 = ttk.Entry(font='Helvetica 56 underline')
ent2 = ttk.Entry()
ent1.grid(row=0, column=0)
ent2.grid(row=1, column=1)
ent1.rowconfigure(0, weight=3)
ent1.columnconfigure(0, weight=30)
ent2.rowconfigure(1, weight=1)

window.grid_propagate(False)

window.mainloop()