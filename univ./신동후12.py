import tkinter
from tkinter import *
win=Tk()
win.geometry('1500x1500')
win.title('Map')

photo1 = PhotoImage(file='africa.png')
photo2 = PhotoImage(file='america.png')
photo3 = PhotoImage(file='asia.png')
photo4 = PhotoImage(file='europe.png')

title = Label(win, text='MAP', font=('Alial',20))
title.pack()

def select():
    if group.get() == 1:
        lbl.configure(image=photo1)
    elif group.get() == 2:
        lbl.configure(image=photo2)
    elif group.get() == 3:
        lbl.configure(image=photo3)
    else:
        lbl.configure(image=photo4)
f= Frame(win)
group = IntVar()
rdol1=Radiobutton(win, text='Africa', variable=group, value=1, command=select)
rdol1.pack()
rdol2=Radiobutton(win, text='America', variable=group, value=2, command=select)
rdol2.pack()
rdol3=Radiobutton(win, text='Africa', variable=group, value=3, command=select)
rdol3.pack()
rdol4=Radiobutton(win, text='Africa', variable=group, value=4, command=select)
rdol4.pack()
rdol1.select()

f.pack()
lbl = Label(win, width=1500, height=1500, bg='gray')
lbl.pack()

win.mainloop()