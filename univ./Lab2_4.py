import accountModule as am
from tkinter import*
win = Tk()
win.title('Account')
win.geometry('300x300')

def deposit():
    ac.deposit(int(e2.get()))
    price = ac.numFormat(int(e2.get()))
    msg = e1.get() + '    '+'   '+price +'   ' +  ac.getBalance()
    lst1.insert(END, msg)
    e1.delete(0, last=len(e1.get()))
    e2.delete(0, last=len(e2.get()))
    l3['text'] = 'total :' +str(lst1.size()-1)
def withdraw():
    ac.withdraw(int(e2.get()))
    price = ac.numFormat(int(e2.get()))
    msg = e1.get() + '    '+'   ''-'+price +'   ' +  ac.getBalance()
    lst1.insert(END, msg)
    e1.delete(0, last=len(e1.get()))
    e2.delete(0, last=len(e2.get()))
    l3['text'] = 'total :' + str(lst1.size() - 1)

ac = am.Account(0,0)

f1 = Frame(win)
f1.pack(fill=BOTH)
l1 = Label(f1, text='Content:',font='Alial 16 bold')
l2 = Label(f1, text='Price:', font='Alial 16 bold')
l1.grid(row=0, column=0)
l2.grid(row=1, column=0)

e1 = Entry(f1,bg='pink', font= 'Alial 16 bold')
e2 = Entry(f1,bg='pink', font= 'Alial 16 bold')
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

f2 = Frame(win)
f2.pack()
b1 = Button(f2, text='deposit', bg='light gray', font='Alial 16 bold', command=deposit)
b1.pack(side=LEFT)
b2 = Button(f2, text='withdraw', bg='light gray', font='Alial 16 bold', command=withdraw)
b2.pack(side=RIGHT)

l3 = Label(win, text='total : 0', font='Alial 10 bold')
l3.pack()

lst1 = Listbox(win, font='helvetica 16 bold', width=10)
lst1.insert(END, 'Content   Price    Balance')
lst1.pack(fill=BOTH)

win.mainloop()
