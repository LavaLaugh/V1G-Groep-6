from tkinter import *
from Basisaplicatie_Back_End import *

def naam_game1():
    naam = naam_game_1()
    label["text"] = "The first game is: {}".format(naam)


def sorting():
    sortEntry.config(state='normal')
    sortlabel["text"] = "How do you want to sort the games?"
    sort = sortEntry.get()
    sorted = sorteren_basis(sort)
    open('Sorted output.txt', 'w').close()
    file = open('Sorted output.txt', 'a')
    for i in sorted:
        string = str(i)
        file.write(string + '\n')



root = Tk()

button = Button(master=root, text="Click here for the first game on Steam", command=naam_game1)
button.pack()

button = Button(master=root, text="Click here for sorting the games", command=sorting)
button.pack()

sortlabel = Label(master=root)

sortEntry = Entry(master=root)
sortEntry.pack()
sortEntry.config(state='readonly')

label = Label(master=root)
label.pack()

root.mainloop()
