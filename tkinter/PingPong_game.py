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
                if self.paddle.movement != 0:
                    if (self.x > 0 and self.paddle.movement > 0) or\
                            (self.x < 0 and self.paddle.movement < 0):
                        self.x = int(self.x * 1.5)
                    elif (self.x < 0 and self.paddle.movement > 0) or\
                            (self.x > 0 and self.paddle.movement < 0):
                        self.x = int(self.x * 0.8)
                        if self.x == 0:
                            self.x += 1
                return True
        return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if int(self.score.text) < 250:
            speed_minus = -4
            speed_plus = 4
        elif int(self.score.text) < 500:
            speed_minus = -5
            speed_plus = 5
        elif int(self.score.text) < 750:
            speed_minus = -6
            speed_plus = 6
            self.paddle.set_speed(-6, 6)
        elif int(self.score.text) < 1000:
            speed_minus = -7
            speed_plus = 7
            self.paddle.set_speed(-7, 7)
        elif int(self.score.text) < 1500:
            speed_minus = -8
            speed_plus = 8
            self.paddle.set_speed(-8, 8)
        else:
            speed_minus = -9
            speed_plus = 9
            self.paddle.set_speed(-9, 9)

        if pos[1] <= 0:
            self.y = speed_plus
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
            self.game_over.show_text()
            self.take_start_position()

        if pos[3] >= self.canvas_height:
            self.y = speed_minus
        if self.hit_paddle(pos) == True:
            self.y = speed_minus

        if pos[0] <= 0:
            self.x = speed_plus
        if pos[2] >= self.canvas_width:
            self.x = speed_minus

    def take_start_position(self):
        pos = self.canvas.coords(self.id)
        while pos[1] > 100:
            pos = self.canvas.coords(self.id)
            self.canvas.move(self.id, 0, -2)
        if pos[0] < 243:
            while pos[0] < 243:
                self.canvas.move(self.id, 2, 0)
                pos = self.canvas.coords(self.id)
        elif pos[0] > 247:
            while pos[0] > 247:
                self.canvas.move(self.id, -2, 0)
                pos = self.canvas.coords(self.id)



class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.move_left = -5
        self.move_right = 5
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<KeyRelease-Left>', self.key_stop)
        self.canvas.bind_all('<KeyRelease-Right>', self.key_stop)
        self.movement = 0

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] < 0:
            self.canvas.move(self.id, self.move_right, 0 )
        if pos[2] > self.canvas_width:
            self.canvas.move(self.id, self.move_left, 0)

    def turn_left(self, evt):
        self.x = self.move_left
        self.movement = -1
    def turn_right(self, evt):
        self.x = self.move_right
        self.movement = 1
    def key_stop(self, evt):
        self.x = 0
        self.movement = 0
    def set_speed(self, s_minus, s_plus):
        self.move_left = s_minus
        self.move_right = s_plus

class Text:
    def __init__(self, canvas, coords, font, color, text, textshow):
        self.canvas = canvas
        self.text = text
        self.textshow = textshow
        self.id = canvas.create_text(*coords, font=font, fill=color, text=text, state=textshow)
    def t_update(self):
        self.text = str(int(self.text) + 10)
        self.canvas.itemconfig(self.id, text=self.text)
    def t_reset(self):
        self.text = str(0)
        self.canvas.itemconfig(self.id, text=self.text)
    def show_text(self):
        time.sleep(0.4)
        self.canvas.itemconfig(self.id, state='normal')
    def hide_text(self):
        self.canvas.itemconfig(self.id, state='hidden')

def start_game(event):
    time.sleep(0.7)
    ball.hit_bottom = False
    game_over.hide_text()
    score.t_reset()



window = Tk()
window.title('PingPong')
window.resizable(False, False)
window.wm_attributes('-topmost', 1)

canvas = Canvas(window, width=500, height=400, bd=0,
                highlightthickness=0)
canvas.pack()
window.bind('<Return>', start_game)
window.update()

score = Text(canvas, (400, 40), ('Helvetica', 16), 'brown', '0', 'normal')
game_over = Text(canvas, (250, 150), ('Helvetica', 30), 'red', 'GAME OVER', 'hidden')
paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, score, game_over, 'red')


while 1:
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
    window.update_idletasks()
    window.update()
    time.sleep(0.02)