import tkinter as tk
from tkinter import *
import requests
from bs4 import BeautifulSoup
from PIL import ImageTk, Image

PyDoviz=tk.Tk()
PyDoviz.title("PY Döviz | Oktay ALA")
PyDoviz.geometry("310x350")
PyDoviz.configure(background='#36454F')

#Logo
logo = ImageTk.PhotoImage(Image.open("logo.png"))
logoimg = Label(PyDoviz, image=logo, background='#36454F')
logoimg.place(x=55,y=10)


#Tarih verilerini çekme#
TARIHhtml = requests.get("https://www.timeanddate.com/worldclock/turkey/istanbul")
TARIHsoup = BeautifulSoup(TARIHhtml.content,features = "lxml")
TARIHtag = TARIHsoup.findAll("span",{"id":"ctdat"})

for TARIH in TARIHtag:
    TARIH_Yazdir = TARIH.text
    TARIHlabel = tk.Label(text=format(TARIH_Yazdir)+" Tarihli TRY kurları",
                        font="Arial 12 bold",
                        fg="white",
                        background='#36454F')
    TARIHlabel.place(x=20,y=60)


#Dolar kuru verileri
USDhtml = requests.get("https://finanswebde.com/doviz/USD")
USDsoup = BeautifulSoup(USDhtml.content,features = "lxml")
USDtag = USDsoup.findAll("span",{"class":"detail-title-md"})

USDsayac = 0
for USD in USDtag:
    USDlogo = ImageTk.PhotoImage(Image.open("USD_Logo.png"))
    USDlogoimg = Label(PyDoviz, image=USDlogo,background='#36454F')
    USDlogoimg.place(x=10,y=100)
    USD_Yazdir = USD.text
    USDlabel = tk.Label(text="USD/TRY: "+USD_Yazdir,
                        font="Arial 20 bold",
                        fg="white",
                        background='#36454F')
    USDlabel.place(x=80,y=110)
    USDsayac += 1
    if USDsayac == 1:
        break


#Euro kuru verileri
EURhtml = requests.get("https://finanswebde.com/doviz/EUR")
EURsoup = BeautifulSoup(EURhtml.content,features = "lxml")
EURtag = EURsoup.findAll("span",{"class":"detail-title-md"})

EURsayac = 0
for EUR in EURtag:
    EURlogo = ImageTk.PhotoImage(Image.open("EUR_Logo.png"))
    EURlogoimg = Label(PyDoviz, image=EURlogo,background='#36454F')
    EURlogoimg.place(x=10,y=180)
    EUR_Yazdir = EUR.text
    EURlabel = tk.Label(text="EUR/TRY: "+EUR_Yazdir,
                        font="Arial 20 bold",
                        fg="white",
                        background='#36454F')
    EURlabel.place(x=80,y=190)
    EURsayac += 1
    if EURsayac == 1:
        break


#Sterlin kuru verileri
GBPhtml = requests.get("https://finanswebde.com/doviz/GBP")
GBPsoup = BeautifulSoup(GBPhtml.content,features = "lxml")
GBPtag = GBPsoup.findAll("span",{"class":"detail-title-md"})

GBPsayac = 0
for GBP in GBPtag:
    GBPlogo = ImageTk.PhotoImage(Image.open("GBP_Logo.png"))
    GBPlogoimg = Label(PyDoviz, image=GBPlogo,background='#36454F')
    GBPlogoimg.place(x=10,y=260)
    GBP_Yazdir = GBP.text
    GBPlabel = tk.Label(text="GBP/TRY: "+GBP_Yazdir,
                        font="Arial 20 bold",
                        fg="white",
                        background='#36454F')
    GBPlabel.place(x=80,y=270)
    GBPsayac += 1
    if GBPsayac == 1:
        break

PyDoviz.mainloop()