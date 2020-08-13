from tkinter import *


def click():
    main.destroy()
    import bot2



main= Tk()   
main.title("LOGIN WINDOW")
main.config(background="black")
main.geometry("1000x600")

main.resizable(0,0)

photo= PhotoImage(file="welcome.png")

kk_label= Label(image = photo)
kk_label.place(x=0,y=0,width=1000,height=200)


Label(main,text="  Hello!! This is my first Bot!  ",fg="Brown",font="Helvatica 20 bold").place(x=600,y=50)
Label(main,text="  Fill these info to continue.. ",bg = "black",fg="white",font="Helvatica 14 bold").place(x=50,y=240)

f1 = Frame(main,bg = "black", borderwidth =8, relief = SUNKEN)
f1.place(x=330,y=300,width=360,height=200)

Label(f1,text="Enter Your Name : ",fg="white",bg = "black",bd= 6,font="Arial 12 bold").place(x=10,y=20)
Label(f1,text="Password : ",fg="white",bg = "black",bd= 6,font="Arial 12 bold").place(x=10,y=60)

e1= Entry(f1)
e1.place(x=180,y=25)
e2= Entry(f1,show='*')
e2.place(x=180,y=70)

Button(main,text="  Signin ",fg="white",bd=3,bg = "black",font="Arial 12 bold",command= click).place(x=420,y=450)
Button(main,text=" Cancel ",fg="white",bd=3,bg = "black",font="Arial 12 bold").place(x=520,y=450)
main.mainloop()
