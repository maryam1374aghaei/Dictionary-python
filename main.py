from tkinter import *
import json
from difflib import get_close_matches
from tkinter import messagebox
import pyttsx3


engine=pyttsx3.init() #creating instance of Engine class

voice=engine.getProperty('voices')
engine.setProperty('voice',voice[0].id)

#Functional Part
def search():
    data=json.load(open('data.json'))
    world=enterworldlabel.get()
    world=world.lower()
    if world in data:
        meaning=data[world]
        print(meaning)
        textarea.delete(1.0,END)
        for item in meaning:
            textarea.insert(END,u'\u2022'+item+'\n\n')
    
    elif len(get_close_matches(world,data.keys()))>0:
        close_match=get_close_matches(world,data.keys())[0]
        res=messagebox.askyesno("cofirm",f'Did you mean? {close_match} instead?')
        if res==True:
            enterworldlabel.delete(0,END)
            enterworldlabel.insert(END,close_match)

            meaning=data[close_match]

            textarea.delete(1.0,END)
            for item in meaning:
                
                textarea.insert(END, u'\u2022' + item + '\n\n')



        else:
            messagebox.showinfo('ERROR','The word dosent exist.')
            enterworldlabel.delete(0,END)
            textarea.delete(1.0,END)
    else:
        messagebox.showinfo('Information','The word dosent exist.')
        enterworldlabel.delete(0,END)
        textarea.delete(1.0,END)


def clear():
    enterworldlabel.delete(0,END)
    textarea.delete(1.0,END)


def iexit():
    res = messagebox.askyesno('Confirm','Did you want to exit?')
    if res == True:
        root.destroy()

    else:
        pass


def worldaudio():
    engine.say(enterworldlabel.get())
    engine.runAndWait()


def meaningaudio():
    engine.say(textarea.get(1.0,END))
    engine.runAndWait()



root = Tk()

root.geometry("1000x626+100+30")
root.title("Dictionary")
root.resizable(True,True)

bgimage=PhotoImage(file="bg.png")
bglable=Label(root,image=bgimage)
bglable.place(x=0,y=0)

enterworldlabel=Label(root,text='Enter Word',font=('Monotype Corsiva',30,'bold'),fg='firebrick1',bg='whitesmoke')
enterworldlabel.place(x=530,y=20)

enterworldlabel=Entry(root,font=('arial',23,'bold'),justify=CENTER,bd=8,relief=GROOVE)
enterworldlabel.place(x=510,y=80)

searchimage=PhotoImage(file='search.png')
searchbutton=Button(root,image=searchimage,bd=0,bg='whitesmoke',cursor='hand2',activebackground='whitesmoke',command=search)
searchbutton.place(x=620,y=150)

micimage=PhotoImage(file='mic.png')
micbutton=Button(root,image=micimage,bd=0,bg='whitesmoke',activebackground='whitesmoke',
                 cursor='hand2',command=worldaudio)
micbutton.place(x=710,y=153)

meaningldlabel=Label(root,text='Meaning',font=('Monotype Corsiva',29,'bold'),fg='firebrick1',bg='whitesmoke')
meaningldlabel.place(x=580,y=240)

textarea=Text(root,width=34,height=8,font=('arial',18,'bold'),bd=8,relief=GROOVE)
textarea.place(x=460,y=300)


audioimage=PhotoImage(file='microphone.png')
audiobutton=Button(root,image=audioimage,bd=0,bg='whitesmoke',activebackground='whitesmoke',
                   cursor='hand2',command=meaningaudio)
audiobutton.place(x=530,y=555)

clearimage=PhotoImage(file='clear.png')
clearbutton=Button(root,image=clearimage,bd=0,bg='whitesmoke',activebackground='whitesmoke',
                   cursor='hand2',command=clear)
clearbutton.place(x=668,y=555)

exitimage=PhotoImage(file='exit.png')
exitbutton=Button(root,image=exitimage,bd=0,bg='whitesmoke',activebackground='whitesmoke',
                  cursor='hand2',command=iexit)
exitbutton.place(x=790,y=555)

def enter_function(event):
    searchbutton.invoke()


root.bind('<Return>',enter_function)

root.mainloop()
