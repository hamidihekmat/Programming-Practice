from tkinter import *
import time
import random
from colors import *
# initializing tkiner or creating instance of the object
tk = Tk()

# make a window
canvas = Canvas(tk, bg='pink',width=500, height=500)
tk.title('Ball')
canvas.pack()


class Ball(object):
    def __init__(self):
        self.ball = canvas.create_oval(10, 10, 60, 60, fill='purple')
        self.xspeed = random.randint(-10,10)
        self.yspeed = random.randint(-10,10)

    def move(self):
        canvas.move(self.ball, self.xspeed, self.yspeed)
        pos = canvas.coords(self.ball)
        if pos[3] > 500:
            self.yspeed = -self.yspeed
            canvas.itemconfig(self.ball, fill=random.choice(color))
        if pos[1] <= 0:
            self.yspeed = -self.yspeed
            canvas.itemconfig(self.ball, fill=random.choice(color))

        if pos[2] >= 500 or pos[0] <=0:
            self.xspeed = -self.xspeed
            canvas.itemconfig(self.ball, fill=random.choice(color))



balls = []

for i in range(40):
    balls.append(Ball())

while True:
    for ball in balls:
        ball.move()
    tk.update()
    time.sleep(0.01)
tk.mainloop()
