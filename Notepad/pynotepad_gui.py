import customtkinter
import tkinter as tk
from tkinter import filedialog, messagebox
import os
import sys
import webbrowser

customtkinter.set_appearance_mode("Light")
customtkinter.set_default_color_theme("blue")

class PyNotepad:
    def __init__(self, master):
        self.master = master
        master.title("pyNotepad | OA")
        master.geometry("800x600")

        self.file = None

        # Menü
        self.menu_bar = tk.Menu(master)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Yeni", command=self.yeni)
        self.file_menu.add_command(label="Kaydet", command=self.kaydet)
        self.file_menu.add_command(label="Aç", command=self.ac)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Çıkış", command=master.quit)
        self.menu_bar.add_cascade(label="Dosya", menu=self.file_menu)

        self.info_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Bilgi", menu=self.info_menu)
        self.info_menu.add_command(label="Geri Bildirim Gönder", command=self.geribildirim)
        self.info_menu.add_command(label="pyNote Hakkında", command=self.hakkinda)

        master.config(menu=self.menu_bar)

        # Metin Alanı
        self.metin_alani = customtkinter.CTkTextbox(master, font=("Consolas", 15))
        self.metin_alani.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    def yeni(self):
        python = sys.executable
        os.execl(python, python, *sys.argv)

    def kaydet(self):
        global file
        if self.file == None:
            self.file = filedialog.asksaveasfilename(initialfile='pyNotepad.txt',
                                                    defaultextension=".txt",
                                                    filetypes=[("Metin Belgeleri", "*.txt")])
            if self.file == "":
                self.file = None

            else:
                f = open(self.file, "w")
                f.write(self.metin_alani.get("1.0", tk.END))
                f.close()

                self.master.title(os.path.basename(self.file) + " - Notepad")
                messagebox.showinfo("pyNotepad", "Dosya başarıyla kaydedildi.")
        else:
            f = open(self.file, "w")
            f.write(self.metin_alani.get("1.0", tk.END))
            f.close()

    def ac(self):
        global file
        self.file = filedialog.askopenfilename(defaultextension=".txt",
                                               filetypes=[("Metin Belgeleri", "*.txt")])
        if self.file == "":
            self.file = None
        else:
            self.master.title(os.path.basename(self.file) + " - Notepad")
            self.metin_alani.delete("1.0", tk.END)
            f = open(self.file, "r")
            self.metin_alani.insert("1.0", f.read())
            f.close()

    def geribildirim(self):
        webbrowser.open("https://www.instagram.com/oktay_ala/", new=1)

    def hakkinda(self):
        messagebox.showinfo("pyNotepad", "Her Hakkı Saklıdır © 2022 | Oktay ALA")

# Ana pencere
pyNotepad = customtkinter.CTk()
notepad = PyNotepad(pyNotepad)
pyNotepad.mainloop()