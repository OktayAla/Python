import tkinter as tk
from tkinter.ttk import *
from tkinter import *
from googletrans import Translator, LANGUAGES
from PIL import ImageTk, Image


#Pencere ayarları#
PyTranslate=tk.Tk()
PyTranslate.title("PY Translate | Çeviri Programı | Oktay ALA")
PyTranslate.geometry("640x260")


#Başlık#
img = ImageTk.PhotoImage(Image.open("Logo.png"))
panel = Label(PyTranslate, image = img)
panel.pack()
#baslik=tk.Label(text="PyTranslate v1.0",font="Arial 20 bold")
#baslik.pack()

#Metin kutusu#
yazigiris = tk.StringVar()
yazigiris=tk.Text(font="Arial 12 bold",bg="white",fg="black")
yazigiris.place(x=10,y=80,width=300,height=120)
yazigiris.insert(tk.END, "")

#Ekran çıktısı#
yazicikis=tk.Text(font="Arial 12 bold",bg="white",fg="black")
yazicikis.place(x=330,y=80,width=300,height=120)

#Dil seçim listesi#
language = list(LANGUAGES.values())
dilsecim1 = tk.StringVar()
dilsecim1.set("Dil Seçin")
combobox_1 = Combobox(master=PyTranslate,textvariable=dilsecim1,values=language)
combobox_1.place(x=90,y=50)

dilsecim2 = tk.StringVar()
dilsecim2.set("Dil Seçin")
combobox_2 = Combobox(master=PyTranslate,textvariable=dilsecim2,values=language)
combobox_2.place(x=410,y=50)

#Çeviri fonksiyonu#
def cevir():
    translator = Translator()
    translated=translator.translate(text= yazigiris.get(1.0, END) , src = dilsecim1.get(), dest = dilsecim2.get())

    yazicikis.delete(1.0, END)
    yazicikis.insert(END, translated.text)


#Temizleme fonksiyonu#
def temizle():
    yazigiris.delete('1.0', END)
    yazicikis.delete('1.0', END)

#Dil seçim yazıları#
dilsecim1label=tk.Label(text="Dil Seçiniz:",font="Arial 10 bold")
dilsecim1label.place(x=10,y=50)
dilsecim2label=tk.Label(text="Dil Seçiniz:",font="Arial 10 bold")
dilsecim2label.place(x=330,y=50)


#Çeviri butonu#
cevirbuton=tk.Button(text="Çevir",font="Arial 13 bold",bg="DarkCyan",fg="white",command=cevir)
#cevirbuton.pack()
cevirbuton.place(x=10, y=220)

#Temizleme butonu#
temizlebuton=tk.Button(text="Temizle",font="Arial 13 bold",bg="LightSeaGreen",fg="white",command=temizle)
#temizlebuton.pack()
temizlebuton.place(x=100, y=220)

PyTranslate.mainloop()