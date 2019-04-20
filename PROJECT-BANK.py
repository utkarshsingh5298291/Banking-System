import sqlite3
from Tkinter import *
from tkMessageBox import *
import random
import time
import splash


splash.splashscreen()
con = sqlite3.Connection('bank_rec')
cur = con.cursor()
cur.execute("create table if not exists accounts (name varchar(30), account_no varchar(30) PRIMARY KEY,address varchar(40), dob varchar(10), nationality varchar(20), gender varchar(8),aadhaar varchar(16) UNIQUE,job varchar(10),phone varchar(20) UNIQUE,email varchar(30) UNIQUE,password varchar(30))" )
root=Tk()

root.geometry("1600x800+0+0")
root.title("Welcome to Custom Bank services.")
root.configure(background='white')

Tops=Frame(root,width=100,bg="black",relief=SUNKEN)
Tops.pack(side=TOP)

localtime=time.asctime(time.localtime(time.time()))
#====================================================================headers==============================================================================================#

l1=Label(Tops,font=('arial',20,'bold'),text='||CB||',fg='red',bg='black',bd=10,anchor='w',justify='left')
l1.grid(row=0,column=0)

l2=Label(Tops,font=('arial',50,'italic'),text='Custom Bank service limited',fg='gold',bg='black',bd=10,anchor='w',justify='left')
l2.grid(row=0,column=1)

l4=Label(Tops,font=('arial',10,'italic'),text=localtime,fg='lime',bg='black',bd=10,anchor='w',justify='left')
l4.grid(row=1,column=0)

l5=Label(Tops,font=('arial',10,'italic'),text='||  ph no.:2223890  ||',fg='white',bg='black',bd=10,anchor='w',justify='left')
l5.grid(row=3,column=0)

l6=Label(Tops,font=('arial',10,'italic'),text='||  address:agra-bombay highway  ||',fg='white',bg='black',bd=10,anchor='w',justify='left')
l6.grid(row=3,column=1)

l7=Label(Tops,font=('arial',10,'italic'),text='||  e-mail:www.xxxBankservice@gamil.com  ||',fg='white',bg='black',bd=10,anchor='w',justify='left')
l7.grid(row=3,column=2)
#================================================================2nd page tkinter=====================================================================================#
#================================================================new account===========================================================================================#
def newaccount():
    root = Tk()
    root.configure(background='dark grey')
    cur.execute("create table if not exists accounts (name varchar(30), account_no varchar(30) PRIMARY KEY,address varchar(40), dob varchar(10), nationality varchar(20), gender varchar(8),aadhaar varchar(16) UNIQUE,job varchar(10),phone varchar(20) UNIQUE,email varchar(30) UNIQUE,password varchar(30))" )
    
    Label(root,text='Enter your account Details :',relief='ridge',font='times 20 bold',fg='green',bg='dark grey').grid()
    Label(root,text='Name:').grid(row=1,column=0,sticky='W')
    e1=Entry(root,width=16,bd=5,font="times 10 bold",justify='right')
    e1.grid(row=1,column=1)

    Label(root,text='Account no.:').grid(row=2,column=0,sticky='W')
    e2=Entry(root,width=16,bd=5,font="times 10 bold",justify='right')
    e2.grid(row=2,column=1)

    Label(root,text='Permanent Address:').grid(row=3,column=0,sticky='W')
    e3=Entry(root,width=16,bd=5,font="times 10 bold",justify='right')
    e3.grid(row=3,column=1)

    Label(root,text='Birth Date:').grid(row=4,column=0,sticky='W')
    e4=Entry(root,width=16,bd=5,font="times 10 bold",justify='right')
    e4.grid(row=4,column=1)

    Label(root,text='Nationality:').grid(row=5,column=0,sticky='W')
    e5=Entry(root,width=16,bd=5,font="times 10 bold",justify='right')
    e5.grid(row=5,column=1)

    Label(root,text='Gender:').grid(row=6,column=0,sticky='W')
    e6=Entry(root,width=16,bd=5,font="times 10 bold",justify='right')
    e6.grid(row=6,column=1)

    Label(root,text='Aadhar card no.:').grid(row=7,column=0,sticky='W')
    e7=Entry(root,width=16,bd=5,font="times 10 bold",justify='right')
    e7.grid(row=7,column=1)

    Label(root,text='Job:').grid(row=8,column=0,sticky='W')
    e8=Entry(root,width=16,bd=5,font="times 10 bold",justify='right')
    e8.grid(row=8,column=1)

    Label(root,text='Phone no.:').grid(row=9,column=0,sticky='W')
    e9=Entry(root,width=16,bd=5,font="times 10 bold",justify='right')
    e9.grid(row=9,column=1)

    Label(root,text='e-mail:').grid(row=10,column=0,sticky='W')
    e10=Entry(root,width=16,bd=5,font="times 10 bold",justify='right')
    e10.grid(row=10,column=1)

    Label(root,text='Password:').grid(row=11,column=0,sticky='W')
    e11=Entry(root,width=16,bd=5,font="times 10 bold",justify='right',show="*")
    e11.grid(row=11,column=1)

    id_fetch = Entry(root)
    id_fetch.grid(row=12, column=0)

    
#===========================================================database new-account====================================================================================================

    def insert():
        cur.execute('insert into accounts values(?,?,?,?,?,?,?,?,?,?,?)',(str(e1.get()), e2.get(), e3.get(),e4.get(), str(e5.get()), str(e6.get()),e7.get(), str(e8.get()), e9.get(),e10.get(), e11.get()))
        con.commit()
        Label(root, text='Inserted').grid(row=13,column=0)
    def show_all():
        ans=cur.execute('select * from accounts').fetchall()
        Label(root, text=ans).grid(row=14,column=0)
        con.commit()

    def show():
        cur.execute('select * from details where code=?',id_fetch.get())
        ans = cur.fetchall()
        con.commit()
        Label(root, text=ans).grid()
    Button(root, text='Insert', command=insert).grid(row=15, column=0)
    Button(root, text='Show', command=show).grid(row=15, column=1)
    Button(root, text='Show All', command=show_all).grid(row=15, column=2)

#================================================================deposit=======================================================================================================
def deposit():
    root=Tk()
    def login1():
                   
        cur = con.cursor()
        p=list(cur.execute("Select * from accounts where account_no='"+str(e12.get())+"'"))
        #print p[0][1],p[0][10]

        if str(e14.get())== p[0][10] and str(e12.get()) == p[0][1] :
        
            showinfo("Successful...","You deposited successfully")
    
    root.configure(background='dark grey')
    Label(root,text='Enter your account Details :',relief='ridge',font='times 20 italic',fg='black',bg='yellow').grid()

    Label(root,text='Account no.:',font='times 10 bold').grid()
    e12=Entry(root,width=16,bd=5,font="times 10 bold")
    e12.grid()
    
    Label(root,text='Deposit amount:',font='times 10 bold').grid()
    e13=Entry(root,width=16,bd=5,font="times 10 bold",justify='right')
    e13.grid()

    Label(root,text='Password:',font='times 10 bold').grid()
    e14=Entry(root,width=16,bd=5,font="times 10 bold",justify='right',show='*')
    e14.grid()
    Button(root,text='OK',width=4,height=2,bd=5,fg='black',bg='yellow',command=login1).grid()
   
    
#=================================================================withdraw=======================================================================================================

def withdraw():
    root=Tk()
    def login2():
                   
        cur = con.cursor()
        q=list(cur.execute("Select * from accounts where account_no='"+str(e15.get())+"'"))
        #print p[0][1],p[0][10]

        if str(e15.get())== str(q[0][1]) and str(e17.get()) == str(q[0][10]) :
            showinfo("Successful...","Your withdrawal is successfully")
    root.configure(background='dark grey')
    Label(root,text='Enter your account Details :',relief='ridge',font='times 20 italic',fg='black',bg='red').grid()

    Label(root,text='Account no.:',font='times 10 bold').grid()
    e15=Entry(root,width=16,bd=5,font="times 10 bold")
    e15.grid()
    
    Label(root,text='Withdraw amount:',font='times 10 bold').grid()
    e16=Entry(root,width=16,bd=5,font="times 10 bold",justify='right')
    e16.grid()

    Label(root,text='Password:',font='times 10 bold').grid()
    e17=Entry(root,width=16,bd=5,font="times 10 bold",justify='right',show='*')
    e17.grid()
    Button(root,text='OK',width=4,height=2,bd=5,fg='white',bg='red',command=login2).grid()
#================================================================check balance=======================================================================================================

def checkbalance():
    root=Tk()
    Label(root,text='Enter your account Details :',relief='ridge',font='times 20 italic',fg='black',bg='red').pack()

    Label(root,text='Account no.:',font='times 10 bold').pack()
    e18=Entry(root,width=16,bd=5,font="times 10 bold").pack()
    
    Label(root,text='Password:',font='times 10 bold').pack()
    e19=Entry(root,width=16,bd=5,font="times 10 bold",justify='right').pack()
#================================================================exit=======================================================================================================

def clear():
    root.destroy()   
#=========================================================BUTTON'S ON THE HOME PAGE=======================================================================================================
    
b1=Button(root,text='New Account',width=20,height=4,bd=10,fg='white',bg='dark khaki',command=newaccount)
b1.pack()
b2=Button(root,text='DEPOSIT',width=20,height=4,bd=10,fg='white',bg='dark khaki',command=deposit)
b2.pack()
b3=Button(root,text='WITHDRAW',width=20,height=4,bd=10,fg='white',bg='dark khaki',command=withdraw)
b3.pack()
b4=Button(root,text='CHECK BALANCE',width=20,height=4,bd=10,fg='white',bg='dark khaki')
b4.pack()
b5=Button(root,text='EXIT',width=20,height=4,bd=10,fg='white',bg='dark khaki',command=clear)
b5.pack()
a=PhotoImage(file='xyz.gif')
Label(root,image=a).pack()

root.mainloop()
