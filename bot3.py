from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import pyttsx3
import speech_recognition as sr
import win32api
from tkinter import *


bot=ChatBot('Alexa')
tr = ListTrainer(bot)

def exit():
    root.destroy()
    import bot4

root= Tk()
root.title(" Chat Bot") 

root.geometry("700x800")

root.resizable(0,0)

photo= PhotoImage(file="mm.png")

kk_label= Label(image = photo)
kk_label.pack(side=TOP,fill="x")

kk=pyttsx3.init()
kk.setProperty('rate', 100)
voices = kk.getProperty('voices')

kk.setProperty('voice',voices[1].id)

chats=open('chat.txt','r').readlines()
tr.train(chats)

def chatting():
    query = e1.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END, "you :" + query)
    msgs.insert(END, "Alexa :",str(answer_from_bot))
    kk.say(answer_from_bot)
    print('Alexa:',answer_from_bot)
    e1.delete(0 , END)
    msgs.yview(END)
    kk.runAndWait()


main_menu= Menu(root)

file_menu= Menu(root)

file_menu.add_command(label='New.. ')
file_menu.add_command(label='Save as..')
file_menu.add_command(label='Exit.. ',command=exit)

main_menu.add_cascade(label='File',menu=file_menu)
main_menu.add_command(label='Edit')
main_menu.add_command(label='Quit')

root.config(menu=main_menu)

f1=Frame(root, relief = SUNKEN)
f1.place(x=6,y=100,height=500,width=670)

e1= Entry (root,bd=6,relief= SUNKEN,font= "Arial 20 bold")
e1.place(x=150,y= 620,height=100,width=530)

Button(root,text="Send",bd=1,width=16,height=6,bg="black",activebackground="lightblue",fg="white",font= "Arial 20 bold",command=chatting).place(x=5,y=620,height=100,width=135)

scrol_y=Scrollbar(root,orient=VERTICAL)
msgs = Listbox(f1 ,fg="white",bg="brown",relief=SUNKEN,borderwidth=10, width=100,height=22, font=("Helvatica",14),yscrollcommand=scrol_y.set)

scrol_y.place(x=675,y=100,height=500)
msgs.pack(side=LEFT, fill=BOTH, pady=10) 



def enter_function(event):
    B1.invoke()


root.bind('<Return>',enter_function)

root.mainloop()

