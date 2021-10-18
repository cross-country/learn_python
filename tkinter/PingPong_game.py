from tkinter import *
import time
import random

class Ball:
    def __init__(self, canvas, paddle, score, game_over, color):
        self.canvas = canvas
        self.paddle = paddle
        self.score = score
        self.game_over = game_over
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = True

    def hit_paddle(self, pos):
        self.paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= self.paddle_pos[0] and pos[0] <= self.paddle_pos[2]:
            if pos[3] >= self.paddle_pos[1] and pos[3] <= self.paddle_pos[3]:
                self.score.t_update()
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
            time.sleep(1)
            #self.сanvas.itemconfig(self.game_over.id, state='normal')

        if pos[3] >= self.canvas_height:
            self.y = -3
        if self.hit_paddle(pos) == True:
            self.y = -2

        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3


class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        if pos[2] >= self.canvas_width:
            self.x = 0

    def turn_left(self, evt):
        self.x = -4
    def turn_right(self, evt):
        self.x = 4

class Text:
    def __init__(self, canvas, coords, font, color, text):
        self.canvas = canvas
        self.text = text
        self.id = canvas.create_text(*coords, font=font, fill=color, text=text)
    def t_update(self):
        self.text = str(int(self.text) + 10)
        self.canvas.itemconfig(self.id, text=self.text)

def start_game(event):
    ball.hit_bottom = False
    canvas.itemconfig(game_over, state='hidden')



window = Tk()
window.title('PingPong')
window.resizable(False, False)
window.wm_attributes('-topmost', 1)

canvas = Canvas(window, width=500, height=400, bd=0,
                highlightthickness=0)
canvas.pack()
window.bind('<Return>', start_game)
window.update()

score = Text(canvas, (400, 40), ('Helvetica', 16), 'brown', '0')
#game_over = canvas.create_text(250, 150, text='GAME OVER', state='hidden',
#                               font=('Helvetica', 30), fill='red')
game_over = Text(canvas, (250, 150), ('Helvetica', 30), 'red', 'GAME OVER')
paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, score, game_over, 'red')


while 1:
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
    window.update_idletasks()
    window.update()
    time.sleep(0.01)