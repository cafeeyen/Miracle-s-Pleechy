from Tkinter import *

root = Tk()
root.title('Miracle\'s Pleechy')

logo = PhotoImage(file="banner.gif")#edit position here
w1 = Label(root, image=logo).grid(row=0,column=0)

explanation = """By Chunyanuch  Kimpiam  57070027 & Yin...."""
w2 = Label(root, 
           justify=LEFT,
           padx = 10, 
           text=explanation).grid(row=1,column=0)

def say():
    print '▀██▀─▄███▄─▀██─██▀██▀▀█'

def Open():
    top = Toplevel()
    # Add a label to the TopLevel, just like you would the root window
    lbl = Label(top, text="Choose Time").grid(row=0)
    count_1 = Button(top, text='1 Minute', width=50).grid(row=1)
    count_2 = Button(top, text='2 Minute', width=50).grid(row=2)

def Quit():
    global root
    root.destroy()

time = Button(text='Set time', width=50, command=Open).grid(row=2, column=0)


game = Button(text='Game start', width=50, command=say).grid(row=3, column=0)

out = Button(text='Quit', width=50, command=Quit).grid(row=4, column=0)

root.mainloop()
