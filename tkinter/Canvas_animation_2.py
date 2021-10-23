import tkinter as tk
import time


window = tk.Tk()



def get_coords():
    ball_x = canvas.coords(ball)[0]
    ball_y = canvas.coords(ball)[1]
    differ_x = mouse_x - ball_x
    differ_y = mouse_y - ball_y
    coords_list = []
    step = 1
    if abs(differ_x) > abs(differ_y) and differ_y != 0:
        tail = abs(differ_x) % abs(differ_y)
        big_step = abs(differ_x) // abs(differ_y)
        period = abs(differ_y)
        if differ_x < 0:
            #tail *= -1
            big_step *= -1

        if differ_y < 0:
            step = -1

        coords_list = [big_step, tail, step, 0, period]
    elif abs(differ_y) > abs(differ_x) and differ_x != 0:
        tail = abs(differ_y) % abs(differ_x)
        big_step = abs(differ_y) // abs(differ_x)
        period = abs(differ_x)
        if differ_y < 0:
            #tail *= -1
            big_step *= -1

        if differ_x < 0:
            step = -1

        coords_list = [step, 0, big_step, tail, period]

    elif differ_x == 0 and differ_y != 0:
        period = abs(differ_y)
        if differ_y < 0:
            step = -1
        coords_list = [0, 0, step, 0, period]

    elif differ_y == 0 and differ_x != 0:
        period = abs(differ_x)
        if differ_x < 0:
            step = -1
        coords_list = [step, 0, 0, 0, period]

    elif differ_x == 0 and differ_y == 0:
        coords_list = [0, 0, 0, 0, 0]

    else:
        print('Something went wrong!')

    return coords_list

def motion():
    step = get_coords()
    if step[0] > 0:
        x_big = step[0] + 1
    elif step[0] < 0:
        x_big = step[0] - 1

    if step[2] > 0:
        y_big = step[2] + 1
    elif step[2] < 0:
        y_big = step[2] - 1

    for i in range(0, int(step[4])):
        if step[1] > 0:
            x = x_big
            step[1] -= 1
        else:
            x = step[0]

        if step[3] > 0:
            y = y_big
            step[3] -= 1
        else:
            y = step[2]
        canvas.move(ball, x, y)
        time.sleep(0.01)
        window.update()
        print(step[0])
    #print(step[1])
    #print(step[2])
    #print(step[3])
    print(step[4])




def move_obj(event):
    global mouse_x
    global mouse_y
    mouse_x = event.x
    mouse_y = event.y
    motion()


canvas = tk.Canvas(width=800, height=500, bg='white')
canvas.pack()
canvas.bind('<Button-1>', move_obj)

ball = canvas.create_oval(40, 40, 150, 150, fill='red', outline='red')

window.mainloop()