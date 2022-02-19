import tkinter as tk
from tkinter import *
import random
import array

pyPassGenerator=tk.Tk()
pyPassGenerator.title("pyPassGenerator | Oktay ALA")
pyPassGenerator.geometry("350x100")

def rastgelesifre():
    sayilar =       ['1','2','3','4','5','6','7','8','9','0']

    kucuk_harfler = ["q","w","e","r","t","y","u",
                     "ı","o","p","ğ","ü","a","s",
                     "d","f","g","h","j","k","l",
                     "ş","i","z","x","c","v","b",
                     "n","m","ö","ç"]

    buyuk_harfler = ["Q","W","E","R","T","Y","U",
                     "I","O","P","Ğ","Ü","A","S",
                     "D","F","G","H","J","K","L",
                     "Ş","İ","Z","X","C","V","B",
                     "N","M","Ö","Ç"]

    semboller =     ["₺","€","$","£",">","<","$","½",
                    "[","]","(",")","=","?","!","/",
                    "*","-","+",":",".",";",",","@",
                    "ß","~","%"]

    karakterler = sayilar + kucuk_harfler + \
                  buyuk_harfler + semboller

    rastgele_sayilar = random.choice(sayilar)
    rastgele_kucuk_harfler = random.choice(kucuk_harfler)
    rastgele_buyuk_harfler = random.choice(buyuk_harfler)
    rastgele_semboller = random.choice(semboller)

    rastgele_karakterler = rastgele_sayilar + rastgele_kucuk_harfler + \
                           rastgele_buyuk_harfler + rastgele_semboller
    max_karakter = 10
    for x in range(max_karakter - 4):
        rastgele_karakterler = rastgele_karakterler + random.choice(karakterler)

        rastgele_karakterler_liste = array.array('u', rastgele_karakterler)
        random.shuffle(rastgele_karakterler_liste)

    sifre = ''
    for x in rastgele_karakterler_liste:
        sifre = sifre + x
    textbox.insert(END,sifre)

def temizle():
    textbox.delete('0', END)

textbox = tk.Entry(font="Arial 20 bold")
textbox.place(x=10,y=10, width=200, height=40)


buton = tk.Button(text="Oluştur",
                  command=rastgelesifre,
                  font="Arial 13 bold",
                  bg="OrangeRed",fg="white")
buton.place(x=10,y=60)
buton.configure()

temizlebuton = tk.Button(text="Temizle",
                  command=temizle,
                  font="Arial 13 bold",
                  bg="Tomato",fg="white")
temizlebuton.place(x=100,y=60)
temizlebuton.configure()

pyPassGenerator.mainloop()