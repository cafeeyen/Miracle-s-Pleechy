from Tkinter import *
from threading import *
from random import *

root = Tk()
root.title('Miracle\'s Pleechy')

explanation = """ Your score  :  """
score = 0
timer = Timer(0, None)

wscore = Label(root, 
           justify=LEFT,
           padx = 10, 
           text=explanation+'0')
wscore.grid(row=1)

wtime = Label(root, 
           justify=LEFT,
           padx = 10, 
           text='Time : %d' % 0)
wtime.grid(row=2)

wask = Label(root, 
           padx = 10, 
           text=' ')
wask.grid(row=3)


def start_time(sec, top):
    """Start timer"""
    #Can't show how many time left
    Quit(top)
    global timer
    timer = Timer(sec, two)
    timer.start()
    start.config(text='Sent', command=check)
    question()
    

def set_time():
    top = Toplevel()
    lbl = Label(top, text="Choose Time").grid(row=0)
    t_1 = Button(top, text='1 Minute', width=50,
                 command=lambda: start_time(60, top)).grid(row=0)
    t_2 = Button(top, text='2 Minute', width=50,
                 command=lambda: start_time(120, top)).grid(row=1)


def question():
    """Make question."""
    global num_a, num_b
    num_a = randint(1, 100)
    num_b = randint(1, 100)
    wask.config(text='%d + %d = ?' % (num_a, num_b))


def check():
    """Check the answer."""
    global num_a, num_b
    if int(ansbox.get()) == num_a + num_b:
        one()
    else:
        two()
    ansbox.delete(0, END)


def one():
    global score
    score += 1
    wscore.config(text=explanation+str(score))
    #Credit art ascii from http://www.heartnsoul.com/ascii_art/sheep.txt
    #http://textart4u.blogspot.com/2013/05/game-over-text-art.html
    print """

        .-:\'  `; `-._ 
       (_,           )
     ,\'o"(            )>
    (__,-\'            )
     (                 )
      `-\'._.------._.-\'
         ///       ///'
      ___________________
     |__ ::___::___::___|
        |  | |  | |  |'
        
    """
    print '\t%d SHEEP JUMP!' % score
    question()
    

def two():
    print """

    ███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
    ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
    ██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
    ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
    ███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄


    ███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
    ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
    ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
    ██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
    ███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
    """
    global score, timer
    score = 0
    timer.cancel()
    start.config(text='Start Game', command=set_time)
    

def Quit(window):
    timer.cancel()
    window.destroy()
    
ansbox = Entry(width=60)
ansbox.grid(row=4)

start = Button(text='Start Game', width=50, command=set_time)
start.grid(row=5)

out = Button(text='Quit', width=50, command=lambda: Quit(root))
out.grid(row=6)

root.mainloop()
