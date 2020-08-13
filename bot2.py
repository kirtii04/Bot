from tkinter import *

def click():
    top.destroy()
    import bot3

top= Tk()
top.title("Second Window") 
top.config(background="brown")
top.geometry("1000x600")


photo= PhotoImage(file="oo.png")

pp_label= Label(image = photo)
pp_label.place(x=680,y=300)

f1 = Frame(top, bg = "white", borderwidth = 15, relief = SUNKEN)
f1.pack(side= TOP,fill="x")


Label(f1,text=" Thank You! To Signin..  ",bg = "white",fg="black",font="Arial 35 bold").pack(fill="y")

Label(top,text=" By clicking here,You can talk to my bot!  ",bg = "lightblue",fg="black",font="Arial 25 bold").place(x=10,y=200)

Button(top, text = "  Click Here..  ",bg = "green",fg="white",font="Arial 22 bold",command=click).place(x=240,y=320)


top.mainloop()
    


