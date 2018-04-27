import os
from tkinter import *

os.system('clear')

def TitleScr():
    win = Tk() #Creates Window
    win.title("Python - Conway's Game of Life")
    win.iconbitmap('favicon.ico')
    w = 800 #Width var for window
    h = 600 #Height var
    sw = win.winfo_screenwidth() #Screen width
    sh = win.winfo_screenheight() #Screen height
    #X & Y of screen
    x = (sw/2) - (w/2)
    y = (sh/2) - (h/2)
    #Set dimensions and position of screen
    win.geometry('%dx%d+%d+%d' % (w, h, x, y))
    win.configure(background='white')
    title = Label(win, text="Conway's Game of Life", font=("Times", 26, "bold"), background="white")
    title.pack()
    title.place(x=225, y=50)
    def GridStart():
        win.destroy() #Destroys title screen window
        gwin = Tk() #Creates new game window
        gwin.title("Python - Conway's Game of Life")
        gw = 800 #Width var for game window
        gh = 600 #Height var
        gsw = gwin.winfo_screenwidth() #Screen width
        gsh = gwin.winfo_screenheight() #Screen height
        #X & Y of screen
        gx = (gsw/2) - (gw/2)
        gy = (gsh/2) - (gh/2)
        #Set dimensions and position of screen
        gwin.geometry('%dx%d+%d+%d' % (w, h, x, y))
        gwin.configure(background='white')
        gtitle = Label(gwin, text="Conway's Game of Life", font=("Times", 26, "bold"), background="white")
        gtitle.pack()
        gtitle.place(x=225, y=50)
        Grid = Label(text=" ", background="gray") #Use Canvas?
        Grid.grid()
        Grid.pack()
        Grid.place(x=150, y=200)
        gwin.mainloop()
    start = Button(win, text="Click to Start!", command=GridStart)
    start.pack()
    start.place(x=345, y=300)
    win.mainloop()
TitleScr()
