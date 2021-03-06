from tkinter import *
from Basisaplicatie_Back_End import *
import sys
import os
import RPi.GPIO as GPIO
GPIO.setmode( GPIO.BCM )
GPIO.setwarnings( 0 )


def restart():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
    
def button_check():
    switch = 23
    GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    while True:
        if( GPIO.input( switch ) ):
            restart()


def game1():
    led = 18
    GPIO.setup(led, GPIO.OUT)
    GPIO.output(led, GPIO.HIGH)
    button1.destroy()
    button2.destroy()
    button3.destroy()
    label1.destroy()
    label2.destroy()
    naam = naam_game_1()
    label["text"] = "De eerste game is: {}".format(naam) + "\nDruk op de knop om terug te gaan"
    GPIO.output(led, GPIO.LOW)
    root.after(100, button_check)


def sorting_input():
    led = 18
    GPIO.setup(led, GPIO.OUT)
    GPIO.output(led, GPIO.HIGH)
    button1.destroy()
    button2.destroy()
    button3.destroy()
    label1.destroy()
    label2.destroy()
    global label21, button21, button22, button23, button24, button25, button26, button27, button28, button29, button291\
        , button292
    label21 = Label(master=root, text="Je kan sorteren op:\n")
    label21.pack()
    button21 = Button(master=root, text="Naam", command=lambda: sorting("name", 1, "Naam"))
    button21.pack()
    button22 = Button(master=root, text="Publicatiedatum", command=lambda: sorting("release_date", 2, "Publicatiedatum"))
    button22.pack()
    button23 = Button(master=root, text="Ontwikkelaar", command=lambda: sorting("developer", 4, "Ontwikkelaar"))
    button23.pack()
    button24 = Button(master=root, text="Uitgever", command=lambda: sorting("publisher", 5, "Uitgever"))
    button24.pack()
    button25 = Button(master=root, text="PEGI", command=lambda: sorting("required_age", 7, "PEGI"))
    button25.pack()
    button26 = Button(master=root, text="Prestaties", command=lambda: sorting("achievements", 11, "Prestaties"))
    button26.pack()
    button27 = Button(master=root, text="Positieve beoordelingen", command=lambda: sorting("positive_ratings", 12, "Positieve beoordelingen"))
    button27.pack()
    button28 = Button(master=root, text="Negatieve beoordelingen", command=lambda: sorting("negative_ratings", 13, "Negatieve beoordelingen"))
    button28.pack()
    button29 = Button(master=root, text="Gemiddelde speeltijd", command=lambda: sorting("average_playtime", 14, "Gemiddelde speeltijd"))
    button29.pack()
    button291 = Button(master=root, text="Eigenaren", command=lambda: sorting("owners", 16, "Eigenaren"))
    button291.pack()
    button292 = Button(master=root, text="Prijs", command=lambda: sorting("price", 17, "Prijs"))
    button292.pack()
    GPIO.output(led, GPIO.LOW)


def sorting(input, x, y):
    led = 18
    GPIO.setup(led, GPIO.OUT)
    GPIO.output(led, GPIO.HIGH)
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
    sorteren_basis(input, x, y)
    file = open('Sorted output.txt')
    lijnen = file.readlines()
    text = ""
    index = 0
    def page(lijnen, text, index):
        for i in lijnen:
            text += str(i)
            index += 1
            if index >= 25:
                return text
    GPIO.output(led, GPIO.LOW)
    root.after(500, button_check)
    label = Label(master=root, text=page(lijnen, text, index) + "\nDe rest is te vinden in Sorted Output.txt")
    label.pack()
    label = Label(master=root, text="\nDruk op de knop om terug te gaan")
    label.pack()

    




def stat_input():
    led = 18
    GPIO.setup(led, GPIO.OUT)
    GPIO.output(led, GPIO.HIGH)
    button1.destroy()
    button2.destroy()
    button3.destroy()
    label1.destroy()
    label2.destroy()
    global label11, button11, button12
    label11 = Label(master=root, text="Je kan statestieken krijgen van:\n")
    label11.pack()
    button11 = Button(master=root, text="PEGI", command=lambda: stat_out("required_age"))
    button11.pack()
    button12 = Button(master=root, text="Prijs", command=lambda: stat_out("price"))
    button12.pack()
    GPIO.output(led, GPIO.LOW)



def stat_out(input):
    led = 18
    GPIO.setup(led, GPIO.OUT)
    GPIO.output(led, GPIO.HIGH)
    label11.destroy()
    button11.destroy()
    button12.destroy()

    label = Label(master=root, text="Het gemiddelde is: " + str(gemiddelde(input)) + "\n")
    label.pack()
    label = Label(master=root, text="Het bereik is: " + str(bereik(input)) + "\n")
    label.pack()
    label = Label(master=root, text="De mediaan is: " + str(mediaan(input, [])) + "\n")
    label.pack()
    label = Label(master=root, text="Het Q1 is: " + str(q1(input)) + "\n")
    label.pack()
    label = Label(master=root, text="Het Q3 is: " + str(q3(input)) + "\n")
    label.pack()
    label = Label(master=root, text="De variantie is: " + str(variantie(input, [])) + "\n")
    label.pack()
    label = Label(master=root, text="De standaardafwijking is: " + str(standaardafwijking(input)) + "\n")
    label.pack()
    label = Label(master=root, text="De frequenties zijn zijn te vinden in Sorted Output.txt\n")
    label.pack()
    label = Label(master=root, text="De modus is: " + str(modus(input)) + "\n")
    label.pack()
    label = Label(master=root, text="Druk op de knop om terug te gaan")
    GPIO.output(led, GPIO.LOW)
    root.after(500, button_check)



root = Tk()

root.geometry("1920x1080")

button1 = Button(master=root, text="Eerste game op Steam", command=game1)
button1.pack()

label1 = Label(master=root)
label1.pack()

button2 = Button(master=root, text="Sorteren", command=sorting_input)
button2.pack()

button3 = Button(master=root, text="Statestiek", command=stat_input)
button3.pack()

label2 = Label(master=root)
label2.pack()

label = Label(master=root)
label.pack()

root.mainloop()




