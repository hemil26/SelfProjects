from tkinter import *
from tkinter import messagebox
import threading
import random
mainscreen =Tk()
mainscreen.geometry('400x300')
mainscreen.title('HANGMAN GAME')
mainscreen.configure(bg='#b8bc86')
photo=PhotoImage(file='HangmanIMG.png')
l=Label(mainscreen,image=photo).pack()



global chance
chance=0
finalCount=0
def play():
    global words
    global selection
    file=open('HangmanWords.txt','r')
    words=file.read().splitlines()
    selection=random.choice(words).upper()

    screen1 =Toplevel(mainscreen)
    screen1.geometry('1100x900')
    screen1.configure(bg='#b8bc86')
    screen1.title('HANGMAN GAME')


    lblWord=StringVar()
    Label(screen1,textvariable=lblWord,bg="#b8bc86",font=("arial",40)).place(x=300,y=460)

    wordWithSpaces='   '.join(selection)
    lblWord.set('   '.join('_'*len(selection)))
    
    global photos
    photos=[PhotoImage(file='h0.png'),PhotoImage(file='h1.png'),PhotoImage(file='h2.png'),PhotoImage(file='h3.png'),PhotoImage(file='h4.png'),PhotoImage(file='h5.png'),PhotoImage(file='h6.png'),PhotoImage(file='h6.png')]
    
   
    imgLabel=Label(screen1,bg='#b8bc86')
    imgLabel.place(x=300,y=-50)
    imgLabel.config(image=photos[0])
    
    def close():
        message=messagebox.askyesno('ALERT','DO YOU WANT TO QUIT THE GAME')
        if(message==True):
            mainscreen.destroy()

    exit1=PhotoImage(file='exit.png')
    exitb=Button(screen1,image=exit1,command=close)
    exitb.place(x=950,y=30)

    
    def check(event):
        global chance
        global selection
        global finalCount
        letter = (event.char).upper()
        if chance<6:
            txt=list(wordWithSpaces)
            guessed=list(lblWord.get())
            if(wordWithSpaces.count(letter)>0):
                for c in range(0,len(txt)):
                    if(txt[c]==letter):
                        guessed[c]=letter
                    lblWord.set(''.join(guessed))
                    if lblWord.get()==wordWithSpaces:
                        message2 = messagebox.askokcancel('YAY!','YOU WON')
                        if(message2==True):
                            mainscreen.destroy()
                        else:
                            pass
            else:
                chance+=1
                imgLabel.config(image=photos[chance])
            
                if(chance==6):
                    answer=messagebox.askokcancel('GAME OVER','YOU LOST')
                    if(answer==True):
                        mainscreen.destroy()
                    else:
                        pass

        
        
    screen1.bind("<Key>",check)  

    screen1.mainloop()





welcome = Label(mainscreen,text='WELCOME TO HANGMAN!!',fg='green',bg='#b8bc86',font=('callibri',18,'bold'))
welcome.place(x=80,y=190)
Button(mainscreen,text='PLAY',fg='green',bg='#b8bc86',font=('callibri',14,'bold'),command=play).place(x=130,y=230)
Button(mainscreen,text='QUIT',fg='green',bg='#b8bc86',font=('callibri',14,'bold'),command=mainscreen.quit).place(x=230,y=230)

mainscreen.mainloop()