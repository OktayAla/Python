import tkinter as tk
from tkinter import *
import random
from PIL import ImageTk, Image

pyDiceGame = Tk()
pyDiceGame.geometry("520x320")
pyDiceGame.title("pyDiceGame | Zar Oyunu | OA")
pyDiceGame.configure(background="#f5f5f5")


background = ImageTk.PhotoImage(Image.open("background.png"))
backgroundimg = Label(pyDiceGame, image=background, background='#f5f5f5')
backgroundimg.place(x=0,y=0)


player1_zar = ['\u2680', '\u2681', '\u2682',
               '\u2683', '\u2684', '\u2685']


player2_zar = ['\u2680','\u2681','\u2682',
               '\u2683','\u2684','\u2685']


def player1_zarsayi(x):
    if x == '\u2680':
        return (1)
    elif x == '\u2681':
        return (2)
    elif x == '\u2682':
        return (3)
    elif x == '\u2683':
        return (4)
    elif x == '\u2684':
        return (5)
    elif x == '\u2685':
        return (6)


def player2_zarsayi(x):
    if x == '\u2680':
        return (1)
    elif x == '\u2681':
        return (2)
    elif x == '\u2682':
        return (3)
    elif x == '\u2683':
        return (4)
    elif x == '\u2684':
        return (5)
    elif x == '\u2685':
        return (6)


def player1_zarat():
    player1_randomZar1 = random.choice(player1_zar)
    player1_randomZar2 = random.choice(player1_zar)

    player1_randomZar1Sayi = player1_zarsayi(player1_randomZar1)
    player1_randomZar2Sayi = player1_zarsayi(player1_randomZar2)

    player1_zarLabel1.configure(text=player1_randomZar1)
    player1_zarLabel2.configure(text=player1_randomZar2)

    player1_zarSayiLabel1.configure(text=player1_randomZar1Sayi)
    player1_zarSayiLabel2.configure(text=player1_randomZar2Sayi)

    global player1_puan
    player1_puan = player1_randomZar1Sayi + player1_randomZar2Sayi
    return player1_puan


def player2_zarat():
    player2_randomZar1 = random.choice(player2_zar)
    player2_randomZar2 = random.choice(player2_zar)

    player2_randomZar1Sayi = player2_zarsayi(player2_randomZar1)
    player2_randomZar2Sayi = player2_zarsayi(player2_randomZar2)

    player2_zarLabel1.configure(text=player2_randomZar1)
    player2_zarLabel2.configure(text=player2_randomZar2)

    player2_zarSayiLabel1.configure(text=player2_randomZar1Sayi)
    player2_zarSayiLabel1.configure(text=player2_randomZar2Sayi)

    global player2_puan
    player2_puan = player2_randomZar1Sayi + player2_randomZar2Sayi
    return player2_puan


def puanhesapla():
    if(player1_puan > player2_puan):
        kazananLabel.configure(text="1. Oyuncu Kazandı")
    elif(player1_puan < player2_puan):
        kazananLabel.configure(text="2. Oyuncu Kazandı")
    elif(player1_puan == player2_puan):
        kazananLabel.configure(text="Oyun berabere.")


puanButon = tk.Button(text="KAZANANI GÖR", font="Arial 10 bold", command=puanhesapla)
puanButon.place(x=200, y=220)

kazananLabel = tk.Label(text="",font="Arial 30 bold")
kazananLabel.place(x=80, y=250)


player1_zarLabel1 = tk.Label(text="", font="Arial 100 bold",fg="#00878f")
player1_zarLabel1.place(x=10, y=50)

player1_zarLabel2 = tk.Label(text="", font="Arial 100 bold",fg="#00878f")
player1_zarLabel2.place(x=110, y=50)

player1_zarSayiLabel1 = tk.Label(text="", font="Times 1")
player1_zarSayiLabel1.place(x=999999, y=999999)

player1_zarSayiLabel2 = tk.Label(text="", font="Times 1")
player1_zarSayiLabel2.place(x=999999, y=999999)

player1_puanZarLabel = tk.Label(text="", font="Arial 20 bold")
player1_puanZarLabel.place(x=40, y=180)

player1_buton1 = tk.Button(text="Zar At", font="Arial 10 bold", command=player1_zarat)
player1_buton1.place(x=85, y=180)


player2_zarLabel1 = tk.Label(text="", font="Arial 100 bold",fg="#e5ad24")
player2_zarLabel1.place(x=300,y=50)

player2_zarLabel2 = tk.Label(text="", font="Arial 100 bold",fg="#e5ad24")
player2_zarLabel2.place(x=400,y=50)

player2_zarSayiLabel1 = tk.Label(text="",font="Times 1")
player2_zarSayiLabel1.place(x=999999,y=999999)

player2_zarSayiLabel2 = tk.Label(text="",font="Times 1")
player2_zarSayiLabel2.place(x=999999,y=999999)

player2_puanZarLabel = tk.Label(text="",font="Arial 20 bold")
player2_puanZarLabel.place(x=340,y=180)

player2_buton1 = tk.Button(text="Zar At",font="Arial 10 bold",command=player2_zarat)
player2_buton1.place(x=380,y=180)


pyDiceGame.mainloop()