import tkinter as tk
from tkinter import *
from math import sqrt

# Ana pencereyi oluşturma
PyCalc = tk.Tk()
PyCalc.title("PY Calc | Oktay ALA")
PyCalc.geometry("300x550")
PyCalc.configure(background="#1e1e1e")

# Sayı giriş kutusu
yazigiris = tk.Entry(font="Arial 24 bold", bg="#333333", fg="white", justify="right", bd=0)
yazigiris.place(x=10, y=10, width=280, height=60)

# Butonlar için stil
buton_stil = {
    "font": "Arial 14 bold",
    "bg": "#444444",
    "fg": "white",
    "bd": 0,
    "activebackground": "#666666",
    "activeforeground": "white"
}

# İşlem butonları için stil
operator_stil = {
    "font": "Arial 14 bold",
    "bg": "#ff9500",
    "fg": "white",
    "bd": 0,
    "activebackground": "#ffaa33",
    "activeforeground": "white"
}

# Temizle butonu için stil
temizle_stil = {
    "font": "Arial 14 bold",
    "bg": "#ff3b30",
    "fg": "white",
    "bd": 0,
    "activebackground": "#ff5e52",
    "activeforeground": "white"
}

# Butonlara tıklama işlevi
def tikla(number):
    current = yazigiris.get()
    yazigiris.delete(0, END)
    yazigiris.insert(0, current + str(number))

def temizle_buton():
    yazigiris.delete(0, END)

def button_equal():
    try:
        result = eval(yazigiris.get())
        yazigiris.delete(0, END)
        yazigiris.insert(0, str(result))
    except:
        yazigiris.delete(0, END)
        yazigiris.insert(0, "Hata !")

def karekok_buton():
    try:
        result = sqrt(float(yazigiris.get()))
        yazigiris.delete(0, END)
        yazigiris.insert(0, str(result))
    except:
        yazigiris.delete(0, END)
        yazigiris.insert(0, "Hata !")

def xkare_buton():
    try:
        result = float(yazigiris.get()) ** 2
        yazigiris.delete(0, END)
        yazigiris.insert(0, str(result))
    except:
        yazigiris.delete(0, END)
        yazigiris.insert(0, "Error")

def yuzde_buton():
    try:
        result = float(yazigiris.get()) / 100
        yazigiris.delete(0, END)
        yazigiris.insert(0, str(result))
    except:
        yazigiris.delete(0, END)
        yazigiris.insert(0, "Error")

# Butonları oluştur
sifir_buton = tk.Button(text="0", **buton_stil, command=lambda: tikla(0))
sifir_buton.place(x=10, y=470, width=190, height=60)

bir_buton = tk.Button(text="1", **buton_stil, command=lambda: tikla(1))
bir_buton.place(x=10, y=400, width=60, height=60)

iki_buton = tk.Button(text="2", **buton_stil, command=lambda: tikla(2))
iki_buton.place(x=80, y=400, width=60, height=60)

uc_buton = tk.Button(text="3", **buton_stil, command=lambda: tikla(3))
uc_buton.place(x=150, y=400, width=60, height=60)

dort_buton = tk.Button(text="4", **buton_stil, command=lambda: tikla(4))
dort_buton.place(x=10, y=330, width=60, height=60)

bes_buton = tk.Button(text="5", **buton_stil, command=lambda: tikla(5))
bes_buton.place(x=80, y=330, width=60, height=60)

alti_buton = tk.Button(text="6", **buton_stil, command=lambda: tikla(6))
alti_buton.place(x=150, y=330, width=60, height=60)

yedi_buton = tk.Button(text="7", **buton_stil, command=lambda: tikla(7))
yedi_buton.place(x=10, y=260, width=60, height=60)

sekiz_buton = tk.Button(text="8", **buton_stil, command=lambda: tikla(8))
sekiz_buton.place(x=80, y=260, width=60, height=60)

dokuz_buton = tk.Button(text="9", **buton_stil, command=lambda: tikla(9))
dokuz_buton.place(x=150, y=260, width=60, height=60)

esittir_buton = tk.Button(text="=", **operator_stil, command=button_equal)
esittir_buton.place(x=220, y=470, width=60, height=60)

arti_buton = tk.Button(text="+", **operator_stil, command=lambda: tikla("+"))
arti_buton.place(x=220, y=400, width=60, height=60)

eksi_buton = tk.Button(text="-", **operator_stil, command=lambda: tikla("-"))
eksi_buton.place(x=220, y=330, width=60, height=60)

carpi_buton = tk.Button(text="×", **operator_stil, command=lambda: tikla("*"))
carpi_buton.place(x=220, y=260, width=60, height=60)

bolme_buton = tk.Button(text="÷", **operator_stil, command=lambda: tikla("/"))
bolme_buton.place(x=220, y=190, width=60, height=60)

karekok_buton = tk.Button(text="√", **operator_stil, command=karekok_buton)
karekok_buton.place(x=150, y=190, width=60, height=60)

xkare_buton = tk.Button(text="x²", **operator_stil, command=xkare_buton)
xkare_buton.place(x=80, y=190, width=60, height=60)

yuzde_buton = tk.Button(text="%", **operator_stil, command=yuzde_buton)
yuzde_buton.place(x=10, y=190, width=60, height=60)

temizle_buton = tk.Button(text="C", **temizle_stil, command=temizle_buton)
temizle_buton.place(x=10, y=120, width=270, height=60)

# Ana döngüyü başlat
PyCalc.mainloop()