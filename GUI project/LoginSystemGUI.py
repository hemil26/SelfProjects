from tkinter import *
from tkinter import messagebox
import os

root = Tk()
root.geometry('500x500')
root.title('LOGIN SCREEN')
root.configure(bg='#CAFFFF')
photo=PhotoImage(file='gui login image.png')
label=Label(root,image=photo).pack()


def registerUser():
    UserName=user_entry.get()
    Pwd=passE.get()
    cPwd=confPass.get()
    EMAIL=email_entry.get()
    
    list_1=os.listdir()
    if(UserName in list_1):
        messagebox.showerror('ERROR','USER ALREADY EXISTS')
    else:
        pass

    if(Pwd==cPwd and '@' in EMAIL and UserName not in list_1):
        file=open(UserName,'w')
        file.write(UserName+'\n')
        file.write(cPwd)
        file.close()
        user_entry.delete(0,END)
        passE.delete(0,END)
        confPass.delete(0,END)
        Label(new_window,text='ACCOUNT IS CREATED',fg='green',bg='#CAFFFF',font=('callibri',14,'bold')).place(x=195,y=205)

    
    if('@' not in EMAIL):
         messagebox.showerror('ERROR','INCORRECT EMAIL')
    else:
        pass
    if(Pwd!=cPwd):
         messagebox.showerror('ERROR','PASSWORD DOESNT MATCH')
    else:
        pass



def login_verify():
    global m
    userV=user1.get()
    pwdV=password1.get()
    user1.delete(0,END)
    password1.delete(0,END)

    list_of_users = os.listdir()
    if(userV in list_of_users):
        file1=open(userV,'r')
        verify=file1.read().splitlines()
        if(pwdV in verify):
            m=Label(loginWindow,text='LOGIN SUCCESSFUL',fg='green',bg='#CAFFFF',font=('callibri',14,'bold'))
            m.place(x=130,y=160)
        else:
            messagebox.showerror('ERROR','INCORRECT PASSWORD')
    else:
        messagebox.showerror('ERROR','USER NOT FOUND')





def login():
    global loginWindow
    global user1
    global password1
    loginWindow=Tk()
    loginWindow.title('LOGIN')
    loginWindow.geometry('400x250')
    loginWindow.configure(bg='#CAFFFF')
    
    Label(loginWindow,text='ENTER YOUR DETAILS BELOW',fg='blue',bg='yellow',font=('callibri',14,'bold')).place(x=90,y=10)

    userL=Label(loginWindow,text='Username:',bg='#CAFFFF')
    userL.place(x=0,y=50)
    passwordL=Label(loginWindow,text='Password:',bg='#CAFFFF')
    passwordL.place(x=3,y=78)

    user1=Entry(loginWindow)
    user1.place(x=75,y=50)
    password1=Entry(loginWindow,show='*')
    password1.place(x=75,y=80)

    Button(loginWindow,text='LOGIN',fg='blue',bg='yellow',font=('callibri',14,'bold'),command=login_verify).place(x=180,y=130)
    loginWindow.mainloop()

        
        
def newmenu():
    but1=Button(root,text='NEW USER',fg='blue',command=newuser)
    but1.place(x=0,y=250)
    but2=Button(root,text='EXISTING USER',fg='blue',command=login)
    but2.place(x=0,y=280)
    but3=Button(root,text='QUIT',fg='blue',command=root.quit)
    but3.place(x=0,y=310)

def newuser():
    global new_window
    new_window=Tk()
    new_window.geometry('500x250')
    new_window.title('NEW USER')
    new_window.configure(bg='#CAFFFF')
    global user_entry
    global email_entry
    global passE
    global confPass
    

    name= Label(new_window,text='Name:',bg='#CAFFFF')
    age=Label(new_window,text='Age:',bg='#CAFFFF')
    email=Label(new_window,text='Email:',bg='#CAFFFF')
    user=Label(new_window,text='Username:',bg='#CAFFFF')
    password=Label(new_window,text='Password:',bg='#CAFFFF')
    repass=Label(new_window,text='Confirm password:',bg='#CAFFFF')
    

    name_entry=Entry(new_window)
    age_entry=Entry(new_window)
    email_entry=Entry(new_window)
    user_entry=Entry(new_window)
    
    name.grid(row=0,sticky=E)
    age.grid(row=1,sticky=E)
    email.grid(row=2,sticky=E)
    user.grid(row=3,sticky=E)
    password.grid(row=4,sticky=E)
    repass.grid(row=5,sticky=E)

    name_entry.grid(row=0,column=1)
    age_entry.grid(row=1,column=1)
    email_entry.grid(row=2,column=1)
    user_entry.grid(row=3,column=1)
    passE=Entry(new_window,show='*')
    passE.grid(row=4,column=1)
    confPass=Entry(new_window,show='*')
    confPass.grid(row=5,column=1)

    Button(new_window,text='Create account',fg='blue',command=registerUser).place(x=220,y=180)


    new_window.mainloop()

start=Button(root,text='START',fg='black',bg='white',command=newmenu)
start.pack()

root.mainloop()