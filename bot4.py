from tkinter import *
def exit():
    main.destroy()

main= Tk()   
main.title("TQ WINDOW")
main.config(background="brown")
main.geometry("800x600")

main.resizable(0,0)

photo= PhotoImage(file="thanq.png")

kk_label= Label(image = photo)
kk_label.pack(side = TOP,fill="x")

Label(main,text="  Have A Great Day!   ",fg="blue",font="Helvatica 14 bold").place(x=600,y=180)


Label(main,text="  Hope to see you again!!   ",bg="brown",fg="black",font="Helvatica 25 bold").place(x=200,y=350)
Button(main,text="  Exit  ",bg="black",fg="white",font="Helvatica 20 bold",bd=5,relief=GROOVE,command=exit).place(x=670,y=510)
main.mainloop()
