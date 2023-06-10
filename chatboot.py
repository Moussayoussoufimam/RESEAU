from tkinter import *
import datetime

root = Tk()

def envoie():
    envoie = "Moi :" +e.get()
    txt.insert(END , "\n" +envoie )

    if 'Bonjour' in e.get():
        txt.insert(END, "\n" + "moussa :Bonjour comment vas=tu? ")

    elif 'heure' in e.get():
        heure = datetime.datetime.now().strftime("%H:%M:%S")
        txt.insert(END , "\n" + "moussa : il est " +heure)


    elif 'nom' in e.get():
        txt.insert(END , "\n" + "moussa : je me nomme moussa " )

    elif 'appelles' in e.get():
        txt.insert(END , "\n" + "moussa : je m'appelle moussa ")
     
    else:
        txt.insert(END , "\n" + "moussa : desole je ne connais pas votre question")
     


    e.delete(0 , END )




txt = Text(root, font=("times new roman", 12))
txt.grid(row=0, column=0, columnspan=2)
e = Entry(root, width=80)
e.grid(row=1, column=0)
envoyer = Button(root, text="Envoyer", command=envoie).grid(row=1, column=1)

root.title("moussa")
root.mainloop()

 

















