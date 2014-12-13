from Tkinter import *
from random import *

root = Tk()
root.title('Miracle\'s Pleechy')

explanation = """ Your score  :  """

state = 0
score = 0
timer = 0
gamebg = PhotoImage(file="pic/main.gif")

wgame = Label(root, image=gamebg)
wgame.grid(row=0)

wscore = Label(root, padx = 10, text=explanation+'0')
wscore.grid(row=1)

wtime = Label(root, padx = 10, text='Time : -')
wtime.grid(row=2)

wask = Label(root, padx = 10, text=' ')
wask.grid(row=3)


def start_time(sec):
    """Start timer"""
    #Can't show how many time left
    bnt_0.destroy()
    gamebg.config(file="pic/jump0.gif")
    global timer, ansbox
    ansbox = Entry(width=60)
    ansbox.grid(row=4)
    timer = sec
    tick()
    wscore.config(text=explanation+str(score))
    bnt_1.config(text='Sent', command=check)
    bnt_2.config(text='Quit', command=root.destroy)
    question()
    

def set_time():
    global bnt_0
    wask.config(text="Choose Time")
    bnt_0 = Button(text='Unlimited', width=50,
                   command=lambda: start_time('Unlimited'))
    bnt_0.grid(row=4)
    bnt_1.config(text='1 Minute', command=lambda: start_time(60))
    bnt_2.config(text='2 Minute', command=lambda: start_time(120))


def tick():
    global timer
    wtime.config(text='Time : %s' % str(timer))
    if timer == 0:
        two()
    elif isinstance(timer, int):
        timer -= 1
        wtime.after(1000, tick)
    

def question():
    """Make question."""
    global num_a, num_b
    num_a = randint(1, 100)
    num_b = randint(1, 100)
    wask.config(text='%d + %d = ?' % (num_a, num_b))


def check():
    """Check the answer."""
    global num_a, num_b
    ans = ansbox.get()
    try:
        int(ans)
    except ValueError:
        ans = ''
    ansbox.delete(0, END)
    if ans == '':
        ansbox.insert(END, '---Please answer---')
    elif float(ans) == num_a + num_b:
        one()
    else:
        two()


def one():
    global score
    score += 1
    wscore.config(text=explanation+str(score))
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
    
    

def two():
    global score, timer, state
    ansbox.destroy()
    gamebg.config(file="pic/main.gif")
    timer = '-'
    tick()
    score, state = 0, 0
    wask.config(text='%d + %d = %d' % (num_a, num_b, num_a + num_b))
    bnt_1.config(text='Start Game', command=set_time)
    

def Quit(window):
    window.destroy()
    

bnt_1 = Button(text='Start Game', width=50, command=set_time)
bnt_1.grid(row=5)

bnt_2 = Button(text='Quit', width=50, command=root.destroy)
bnt_2.grid(row=6)

root.mainloop()
