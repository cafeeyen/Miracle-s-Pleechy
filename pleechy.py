from Tkinter import *
from threading import *

root = Tk()
root.title('Miracle\'s Pleechy')

explanation = """ Your score  :  """
score = 0
timer = Timer(0, None)

wscore = Label(root, 
           justify=LEFT,
           padx = 10, 
           text=explanation+'0').grid(row=1,column=0)

wtime = Label(root, 
           justify=LEFT,
           padx = 10, 
           text='Time : %d' % 0).grid(row=2,column=0)

space = Label(root, 
           justify=LEFT,
           padx = 10, 
           text=' ').grid(row=3,column=0)


def start_time(sec, top):
    """Start timer"""
    #Can't show how many time left
    Quit(top)
    global timer
    timer = Timer(sec, two)
    timer.start()
    

def set_time():
    top = Toplevel()
    lbl = Label(top, text="Choose Time").grid(row=0)
    count_1 = Button(top, text='1 Minute',
                     width=50, command=lambda: start_time(60, top)).grid(row=1)
    count_2 = Button(top, text='2 Minute',
                     width=50, command=lambda: start_time(120, top)).grid(row=2)


def one():
    global score
    score += 1
    wscore = Label(root, 
           justify=LEFT,
           padx = 10, 
           text=explanation+str(score)).grid(row=1,column=0)
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
    

def Quit(window):
    window.destroy()
    

start = Button(text='Start Game', width=50,
               command=set_time).grid(row=4, column=0)

correct = Button(text='Correct', width=50,
                 command=one).grid(row=5, column=0)

wrong = Button(text='Wrong', width=50,
               command=two).grid(row=6, column=0)

out = Button(text='Quit', width=50,
             command=lambda: Quit(root)).grid(row=7, column=0)

root.mainloop()
