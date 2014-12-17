"""PSIT Project - Miracle's Pleechy
By Chunyanuch 57070027 & Suttinee 57070113
"""

from Tkinter import *
from random import randint

root = Tk()
root.title("Miracle\'s Pleechy")
root.config(bg="black")

def set_time():
    """Choose time to play."""
    global btn_0
    wask.config(text="Choose Time")
    btn_0 = Button(image=btn_img_0, bg="black", activebackground="black",\
                   borderwidth=0, command=lambda: start_time("Unlimited"))
    btn_0.grid(row=4)
    btn_img_1.config(file="pic/1.gif")
    btn_1.config(command=lambda: start_time(60))
    btn_img_2.config(file="pic/2.gif")
    btn_2.config(command=lambda: start_time(120))


def start_time(sec):
    """Start timer."""
    global timer, ansbox
    btn_0.destroy()
    gamebg.config(file="pic/jump0.gif")
    ansbox.grid(row=4)
    
    timer = sec
    tick()
    
    btn_img_1.config(file="pic/sent.gif")
    btn_1.config(command=check)
    btn_img_2.config(file="pic/quit.gif")
    btn_2.config(command=root.destroy)
    
    question()
    

def tick():
    """Count timer."""
    global timer
    wtime.config(text="Time : %s" % str(timer))
    if timer == 0:
        two()
    elif isinstance(timer, int):
        timer -= 1
        wtime.after(1000, tick)
    

def question():
    """Make question."""
    global num_a, num_b, ran
    sign = ["+", "-"]
    num_a = randint(1, 100)
    num_b = randint(1, 100)
    ran = randint(0, 1)
    wask.config(text="%d %s %d = ?" % (num_a, sign[ran], num_b))


def check():
    """Check the answer."""
    global num_a, num_b, ran
    ans = ansbox.get()
    ansbox.delete(0, END)
    
    try:
        int(ans)
    except ValueError:
        ans = ""
        
    if ans == "":
        ansbox.insert(END, "---Please answer number---")
    elif (ran == 0 and float(ans) == num_a + num_b) or\
         (ran == 1 and float(ans) == num_a - num_b):
        correct()
    else:
        wrong()


def correct():
    """Sheep jump and get score when correct"""
    global score
    score += 1
    wscore.config(text=" Your score  :  %d" % score)
    jump()
    question()


def jump():
    """Sheep jump when correct"""
    global state
    gamebg.config(file="pic/jump%d.gif" % state)
    state += 1
    if state == 5:
        state = 0
        gamebg.config(file="pic/jump%d.gif" % state)
        return 0
    wgame.after(75, jump)


def wrong():
    """Game over when wrong"""
    global score, timer, state, ran
    ansbox.destroy()
    gamebg.config(file="pic/main.gif")
    timer = "Game Over"
    tick()
    score, state = 0, 0
    if ran == 0:
        wask.config(text="%d + %d = %d" % (num_a, num_b, num_a + num_b))
    else:
        wask.config(text="%d - %d = %d" % (num_a, num_b, num_a - num_b))
    btn_img_1.config(file="pic/start.gif")
    btn_1.config(command=set_time)


state, score , timer = 0, 0, 0

gamebg = PhotoImage(file="pic/main.gif")
btn_img_0 = PhotoImage(file="pic/un.gif")
btn_img_1 = PhotoImage(file="pic/start.gif")
btn_img_2 = PhotoImage(file="pic/quit.gif")

wgame = Label(root, image=gamebg, borderwidth=0)
wscore = Label(root, text=" Your score  :  0", fg="white", bg="black")
wtime = Label(root, text="Time : -", fg="white", bg="black")
wask = Label(root, text="Welcome", fg="white", bg="black")

ansbox = Entry(width=60)

btn_1 = Button(image=btn_img_1, bg="black", activebackground="black",\
               borderwidth=0, command=set_time)
btn_2 = Button(image=btn_img_2, bg="black", activebackground="black",\
               borderwidth=0, command=root.destroy)

wgame.grid(row=0)
wscore.grid(row=1)
wtime.grid(row=2)
wask.grid(row=3)
btn_1.grid(row=5)
btn_2.grid(row=6)

root.mainloop()
