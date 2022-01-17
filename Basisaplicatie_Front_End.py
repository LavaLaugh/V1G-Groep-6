from tkinter import *
from Basisaplicatie_Back_End import *
#import RPi.GPIO as GPIO
#import time
#GPIO.setmode( GPIO.BCM )
#GPIO.setwarnings( 0 )

def game1():
    button1.destroy()
    button2.destroy()
    label1.destroy()
    label2.destroy()
    naam = naam_game_1()
    label["text"] = "The first game is: {}".format(naam)


def sorting_input():
    print(input)
    button1.destroy()
    button2.destroy()
    label1.destroy()
    label2.destroy()
    global label21, button21, button22, button23, button24, button25, button26, button27, button28, button29, button291\
        , button292
    label21 = Label(master=root, text="Je kan sorteren op:\n")
    label21.pack()
    button21 = Button(master=root, text="Naam", command=lambda: sorting("name"))
    button21.pack()
    button22 = Button(master=root, text="Publicatiedatum", command=lambda: sorting("release_date"))
    button22.pack()
    button23 = Button(master=root, text="Ontwikkelaar", command=lambda: sorting("developer"))
    button23.pack()
    button24 = Button(master=root, text="Uitgever", command=lambda: sorting("publisher"))
    button24.pack()
    button25 = Button(master=root, text="PEGI", command=lambda: sorting("required_age"))
    button25.pack()
    button26 = Button(master=root, text="Prestaties", command=lambda: sorting("achievements"))
    button26.pack()
    button27 = Button(master=root, text="Positieve beoordelingen", command=lambda: sorting("positive_ratings"))
    button27.pack()
    button28 = Button(master=root, text="Negatieve beoordelingen", command=lambda: sorting("negative_ratings"))
    button28.pack()
    button29 = Button(master=root, text="Gemiddelde speeltijd", command=lambda: sorting("average_playtime"))
    button29.pack()
    button291 = Button(master=root, text="Eigenaren", command=lambda: sorting("owners"))
    button291.pack()
    button292 = Button(master=root, text="Prijs", command=lambda: sorting("price"))
    button292.pack()

def sorting(input):
    label21.destroy()
    button21.destroy()
    button22.destroy()
    button23.destroy()
    button24.destroy()
    button25.destroy()
    button26.destroy()
    button27.destroy()
    button28.destroy()
    button29.destroy()
    button291.destroy()
    button292.destroy()
    sorteren_basis(input)
    label = Label(master=root, text="De gesorteerde lijst is te vinden in Sorted output.txt")
    label.pack()




b = 1
root = Tk()

root.geometry("426x240")

button1 = Button(master=root, text="Click here for the first game on Steam", command=game1)
button1.pack()

label1 = Label(master=root)
label1.pack()

button2 = Button(master=root, text="Click here for sorting the games", command=sorting_input)
button2.pack()

label2 = Label(master=root)
label2.pack()

label = Label(master=root)
label.pack()

root.mainloop()




"""switch = 23
GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
while True:
   if(GPIO.input(switch)):
       sorting()"""