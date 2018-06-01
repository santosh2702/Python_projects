import random
import tkinter as tk

window =tk.Tk()

window.geometry("800x800")
window.title("Sorting Hat")

#-----Functions------
def phrase_generator():
    phrases =["Gryffindor!","Slythrin!","Hufflepuff!","RavenClaw!"]

    name = str(entry1.get())
    if(name =="Saumya"):
        return "You are the greatest wizard ever born on this earth!" + "\n\t" + ";)"
    else:
        return name + " belongs to "+ phrases[random.randint(0,3)]


def phrase_display():
    teller = phrase_generator()
    # text field

    teller_display = tk.Text(master = window, height =10, width =33,font =("Helvetica 10 bold italic",15),pady =30, padx =10)
    teller_display.grid(column =0,row =3)
    teller_display.insert(tk.END, teller)



#-------LABEL-------
label1 = tk.Label(text= "Ever wondered which house you'd be in if you went to Hogwarts?")
label1.grid(column =0,row =0)

label2 = tk.Label(text= "What is your name?",font = ("Times New Roman",20))
label2.grid(column =0, row =1)

#----------ENTRY FIELD------------
entry1 = tk.Entry()
entry1.focus_set()

entry1.grid(column =1,row =1)

#------------BUTTON-------------

button1 = tk.Button(text = "Click here",command = phrase_display)
button1.grid(column =0, row =2)




window.mainloop()