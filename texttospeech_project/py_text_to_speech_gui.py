import tkinter as tk
from tkinter import *
from gtts import gTTS
from playsound import playsound
import playsound as sp
import sys
import os

PyTextToSpeech=tk.Tk()
PyTextToSpeech.title("PY Text To Speech | Oktay ALA")
PyTextToSpeech.geometry("400x250")
PyTextToSpeech.configure(background='LightYellow')

baslik=tk.Label(text="Py-TextToSpeech",
				font="Arial 30 bold",
				bg="LightYellow",
				fg="SaddleBrown")
baslik.pack()

yazilabel = tk.Label(text="Yazı Giriniz: ",
					 font="Arial 10 bold",
					 bg="LightYellow",
					 fg="SaddleBrown")

yazilabel.place(x=10,y=80)
yazigiris = tk.Entry(font="Arial 12 bold")
yazigiris.place(x=10,y=100,width=380,height=40)

def konus():
    sesdosyasi = 'speech.mp3'
    dil = 'tr'
    konusfunc = gTTS(text = yazigiris.get(),lang = dil)
    konusfunc.save(sesdosyasi)
    playsound(sesdosyasi)

#def temizle():
    #yazigiris.delete(0, END)

def yenidenbaslat():
    python = sys.executable
    os.execl(python, python, * sys.argv)

konusbuton=tk.Button(text="KONUŞ",
				 font="Arial 10 bold",
				 bg="BurlyWood",
				 fg="SaddleBrown",
				 command=konus)
konusbuton.place(x=20, y=150, width=350, height=30)

temizlebuton=tk.Button(text="TEMİZLE",
				 font="Arial 10 bold",
				 bg="BurlyWood",
				 fg="SaddleBrown",
				 command=yenidenbaslat)
temizlebuton.place(x=20, y=200, width=350, height=30)

PyTextToSpeech.mainloop()