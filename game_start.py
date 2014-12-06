from Tkinter import *

root = Tk()
root.title('Miracle\'s Pleechy')


explanation = """ Your score  :  """
score = 0
w1 = Label(root, 
           justify=LEFT,
           padx = 10, 
           text=explanation+str(score)).grid(row=1,column=0)
           
#Don't have time setting

w2 = Label(root, 
           justify=LEFT,
           padx = 10, 
           text='Time : ').grid(row=2,column=0)

space = Label(root, 
           justify=LEFT,
           padx = 10, 
           text=' ').grid(row=3,column=0)

def one():
    global score
    score += 1
    w1 = Label(root, 
           justify=LEFT,
           padx = 10, 
           text=explanation+str(score)).grid(row=1,column=0)
    #Credit art ascii from http://www.heartnsoul.com/ascii_art/sheep.txt
    #http://textart4u.blogspot.com/2013/05/game-over-text-art.html
    print ' '
    print ' '
    print '    .-:\'  `; `-._ '
    print '   (_,           )'
    print ' ,\'o"(            )>'
    print '(__,-\'            )'
    print ' (                 )'
    print '  `-\'._.------._.-\''
    print '     ///       ///'
    print '  ___________________'
    print ' |__ ::___::___::___|'
    print '    |  | |  | |  |'
    print ' '
    print '    '+str(score) + ' SHEEP JUMP!'

def two():
    print ' '
    print ' '
    print '███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀'
    print '██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼'
    print '██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀'
    print '██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼'
    print '███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄'
    print ' '
    print ' '
    print '███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼'
    print '██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼'
    print '██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼'
    print '██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼'
    print '███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄'

def Quit():
    global root
    root.destroy()

correct = Button(text='correct', width=50, command=one).grid(row=4, column=0)

wrong = Button(text='wrong', width=50, command=two).grid(row=5, column=0)

out = Button(text='Quit', width=50, command=Quit).grid(row=6, column=0)

root.mainloop()
