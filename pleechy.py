from Tkinter import *
from random import *

root = Tk()
root.title('Miracle\'s Pleechy')

explanation = """ Your score  :  """
name = """
    By Chunyanuch 57070027 & Suttinee 57070113
    """

state = 0
score = 0
timer = 0
logo = PhotoImage(file="banner.gif")#edit position here
sheep = PhotoImage(file="sheep jump/%d.gif" % state)

wlogo = Label(root, image=logo).grid(row=0)
wname = Label(root, text=name).grid(row=1)

wscore = Label(root, padx = 10, text=explanation+'0')
wscore.grid(row=2)

wtime = Label(root, padx = 10, text='Time : -')
wtime.grid(row=3)

wask = Label(root, padx = 10, text=' ')
wask.grid(row=4)

wgame = Label(root, image=sheep)
wgame.grid(row=5)


def start_time(sec):
    """Start timer"""
    #Can't show how many time left
    global timer
    timer = sec
    tick()
    sheep.config(file="sheep jump/1.gif")
    bnt_1.config(text='Sent', command=check)
    bnt_2.config(text='Quit', command=root.destroy)
    question()
    

def set_time():
    lbl = Label(text="Choose Time")
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
    sheep.config(file="sheep jump/%d.gif" % state)
    state += 1
    if state == 6:
        state = 1
        sheep.config(file="sheep jump/%d.gif" % state)
        return 0
    wgame.after(100, jump)
    
    

def two():
    sheep.config(file="game over/0.gif")
    global score, timer, state
    timer = '-'
    tick()
    score, state = 0, 0
    bnt_1.config(text='Start Game', command=set_time)
    
    
ansbox = Entry(width=60)
ansbox.grid(row=6)

bnt_1 = Button(text='Start Game', width=50, command=set_time)
bnt_1.grid(row=7)

bnt_2 = Button(text='Quit', width=50, command=root.destroy)
bnt_2.grid(row=8)

root.mainloop()
