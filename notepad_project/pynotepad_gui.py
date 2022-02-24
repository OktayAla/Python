import tkinter as tk
from tkinter import *
from tkinter import filedialog,messagebox
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
import sys
import webbrowser

pyNotepad=tk.Tk()
pyNotepad.title("pyNotepad | OA")
pyNotepad.geometry("600x600")

sb = Scrollbar(pyNotepad)
sb.pack(side=RIGHT, fill=Y)

metin_alani = tk.Text(font="Consolas 15",yscrollcommand=sb.set)
file = None
metin_alani.pack(expand=True, fill=BOTH)

def yeni():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def kaydet():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='pyNotepad.txt',
                                 defaultextension=".txt",
                                 filetypes=[("Metin Belgeleri", "*.txt")])
        if file == "":
            file = None

        else:
            f = open(file, "w")
            f.write(metin_alani.get(1.0, END))
            f.close()

            pyNotepad.title(os.path.basename(file) + " - Notepad")
            messagebox.showinfo("pyNotepad", "Dosya başarıyla kaydedildi.")
    else:
        f = open(file, "w")
        f.write(metin_alani.get(1.0, END))
        f.close()

def ac():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("Metin Belgeleri", "*.txt")])
    if file == "":
        file = None
    else:
        pyNotepad.title(os.path.basename(file) + " - Notepad")
        metin_alani.delete(1.0, END)
        f = open(file, "r")
        metin_alani.insert(1.0, f.read())
        f.close()

def geribildirim():
    webbrowser.open("https://www.instagram.com/oktay_ala/", new=1)

def hakkinda():
    messagebox.showinfo("pyNotepad", "Her Hakkı Saklıdır © 2022 | Oktay ALA")

ust_menu = Menu(pyNotepad)
ust_menu_dosya = Menu(ust_menu, tearoff=0)
ust_menu.add_cascade(label="Dosya", menu=ust_menu_dosya)
ust_menu_dosya.add_command(label="Yeni",command=yeni)
ust_menu_dosya.add_command(label="Kaydet",command=kaydet)
ust_menu_dosya.add_command(label="Aç",command=ac)
ust_menu_dosya.add_separator()
ust_menu_dosya.add_command(label="Çıkış", command=pyNotepad.quit)

ust_menu_bilgi = Menu(ust_menu, tearoff=0)
ust_menu.add_cascade(label="Bilgi", menu=ust_menu_bilgi)
ust_menu_bilgi.add_command(label="Geri Bildirim Gönder",command=geribildirim)
ust_menu_bilgi.add_command(label="pyNote Hakkında",command=hakkinda)

pyNotepad.config(menu=ust_menu)


pyNotepad.mainloop()