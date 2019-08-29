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

ball = canvas.create_oval(10, 10, 60, 60, fill='purple')

# acceleration
xspeed = 4
yspeed = 8



while True:
    canvas.move(ball, xspeed, yspeed)
    pos = canvas.coords(ball)
    if pos[3] > 500:
        yspeed = -yspeed
        canvas.itemconfig(ball, fill=random.choice(color))
    if pos[1] <= 0:
        yspeed = -yspeed
        canvas.itemconfig(ball, fill=random.choice(color))

    if pos[2] >= 500 or pos[0] <=0:
        xspeed = -xspeed
        canvas.itemconfig(ball, fill=random.choice(color))

    tk.update()
    time.sleep(0.01)
tk.mainloop()
