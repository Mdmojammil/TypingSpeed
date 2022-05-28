words=['grapes','Mango','Apple','gun','fan','door','tv','mobile','laptop']



def labelslider():
    global count,sliderwords
    text = 'Welcome to typing increser Game'
    if(count>=len(text)):
        count=0
        sliderwords=''
    sliderwords += text[count]
    count +=1
    fontlabel.config(text=sliderwords)
    fontlabel.after(150,labelslider)

def time():
    global timeleft,score,miss
    if(timeleft>=11):
        pass
    else:
        timerLabelCount.configure(fg='red')
    if(timeleft>=0):
        timeleft -=1
        timerLabelCount.configure(text=timeleft)
        timerLabelCount.after(1000,time)

    else:
        gameplayDetailLabel.configure(text='Hit={}| Miss={} | Total Score={}'.format(score,miss,score-miss))
        rr=messagebox.askretrycancel('Notification','For Play Again Hit Retry Button')
        if(rr==True):
            score=0
            timeleft=60
            miss=0
            timerLabelCount.configure(text=words[0])
            scoreLabelCount.configure(text=score)


def startGame(event):
    global score,miss
    if(timeleft==60):
         time()
    gameplayDetailLabel.configure(text='')
    if(wordEntry.get()==wordLabel['text']):
        score +=1
        scoreLabelCount.configure(text=score)
    else:
        miss +=1
    random.shuffle(words)
    wordLabel.configure(text=words[0])

    wordEntry.delete(0,END)

from tkinter import *
import random
from tkinter import messagebox
####################################root method
root=Tk()
root.geometry('800x600+400+100')
root.config(bg='powder blue')
root.title('typing speed increser Game')
##################################  variables
score=0
timeleft=60
count=0
sliderwords=''
miss=0

#############################label methods
fontlabel=Label(root,text='',font=('arial',25,'italic bold'),
                bg='powder blue',fg='red',width=40)
fontlabel.place(x=10,y=10)
labelslider()
random.shuffle(words)

wordLabel=Label(root,text=words[0],font=('arial',40,'italic bold'),bg='powder blue')
wordLabel.place(x=350,y=200)

scoreLabel=Label(root,text='Your score:',font=('arial',25,'italic bold'),bg='powder blue')
scoreLabel.place(x=10,y=100)

scoreLabelCount=Label(root,text=score,font=('arial',25,'italic bold'),bg='powder blue',fg='blue')
scoreLabelCount.place(x=80,y=180)

timerLabel=Label(root,text='Time Left',font=('arial',25,'italic bold'),bg='powder blue')
timerLabel.place(x=600,y=100)

timerLabelCount=Label(root,text=60,font=('arial',25,'italic bold'),bg='powder blue',fg='blue')
timerLabelCount.place(x=680,y=180)

gameplayDetailLabel=Label(root,text='Type word And Hit Enter Button',font=('arial',30,'italic bold'),
                          bg='powder blue',fg='dark grey')
gameplayDetailLabel.place(x=120,y=450)






###################################Entry box
wordEntry=Entry(root,font=('arial',25,'italic bold'),bd=10,justify='center')
wordEntry.place(x=250,y=300)
wordEntry.focus_set()

#############################################
root.bind('<Return>',startGame)
root.mainloop()