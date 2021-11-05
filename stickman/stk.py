from tkinter import *
import time
import random

class Game:
    def __init__(self):
        self.tk = Tk()
        self.tk.title('A human hurries to the exit')
        self.tk.resizable(0, 0)
        self.tk.wm_attributes('-topmost', 1)
        self.canvas = Canvas(self.tk, width=500, height=500, \
                             highlightthickness=0)
        self.canvas.pack()
        self.tk.update()
        self.canvas_height = 500
        self.canvas_width = 500
        self.bg = PhotoImage(file='background.gif')
        self.bg1 = PhotoImage(file='task1.gif')
        self.bg2 = PhotoImage(file='task2.gif')
        self.bg3 = PhotoImage(file='task3.gif')
        self.bg4 = PhotoImage(file='task4.gif')

        w = self.bg.width()
        h = self.bg.height()
        background_list = [self.bg]
        background_list.append(self.bg1)
        background_list.append(self.bg2)
        background_list.append(self.bg3)
        background_list.append(self.bg4)

        print(len(background_list))
        for x in range(0, 5):
            for y in range(0, 5):
                random.shuffle(background_list)
                self.canvas.create_image(x * w, y * h , \
                                         image=background_list[0], anchor='nw')


        self.sprites = []
        self.running = True
    def mainloop(self):
        while 1:
            if self.running == True:
                for sprite in self.sprites:
                    sprite.move()
            self.tk.update_idletasks()
            self.tk.update()
            time.sleep(0.01)


g = Game()
g.mainloop()