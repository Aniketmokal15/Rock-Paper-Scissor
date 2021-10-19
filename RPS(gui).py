from tkinter import *
from tkinter import ttk
import random


root=Tk()
root.geometry("720x450")
root.title("Rock Paper Scissor")


computer_options = {"0":"Rock","1":"Paper","2":"Scissor"}

def rock():
    value = computer_options[str(random.randint(0, 2))]
    if value == "Rock":
        match_result = "Match Draw"
    elif value == "Scissor":
        match_result = " You Won"
    else:
        match_result = "Computer Win"
    b1.config(text=match_result)
    l1.config(text="Rock")
    l3.config(text=value)
def paper():
    value = computer_options[str(random.randint(0, 2))]
    if value == "Paper":
        match_result = "Match Draw"
    elif value == "Scissor":
        match_result = "Computer Win"
    else:
        match_result = "You win"
    b1.config(text=match_result)
    l1.config(text="Paper")
    l3.config(text=value)
def scissor():
    value = computer_options[str(random.randint(0, 2))]
    if value == "Rock":
        match_result = "Computer Win"
    elif value == "Scissor":
        match_result = "Match Draw"
    else:
        match_result = "You Win"
    b1.config(text=match_result)
    l1.config(text="Scissor")
    l3.config(text=value)








###Label frame
labelframe= LabelFrame(root, text= "Rock Paper Scissor",bg="white", fg="black", bd=15,
                          font=("Comic Sans MS", 15), padx=2, pady=6)
labelframe.pack(expand= True, fill= BOTH)




##buttons
pic1=PhotoImage(file="fst.png")
b1=Button(labelframe,text="Click me",image=pic1,command= rock)
b1.place(x=100,y=50)


pic2=PhotoImage(file="paper.png")
b2=Button(labelframe,text="Click me",image=pic2,command=paper)
b2.place(x=300,y=50)


pic3=PhotoImage(file="ssr.png")
b3= Button(labelframe, text= "Scissor", image=pic3, command= scissor)
b3.place(x=500,y=50)


###button for result
b1= Label(labelframe, text="", font=('Coveat', 25,'bold'), bg= "white",fg="black")
b1.place(x=300,y=150)

###labels for comp vs user

l1= Label(labelframe, text="USER", font=("Comic Sans MS", 18))
l1.place(x=100,y=250)



l2= Label(labelframe, text="v/s", font=("Comic Sans MS", 18))
l2.place(x=310,y=250)


l3= Label(labelframe, text="COMP", font=("Comic Sans MS", 18))
l3.place(x=500,y=250)


root.mainloop()