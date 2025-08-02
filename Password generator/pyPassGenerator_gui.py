import customtkinter
import random
import pyperclip  # Panoya kopyalama için

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


def rastgelesifre():
    """Rastgele şifre oluşturur ve textbox'a yazdırır."""
    sayilar = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    kucuk_harfler = ["q", "w", "e", "r", "t", "y", "u", "ı", "o", "p", "ğ", "ü", "a", "s", "d", "f", "g", "h", "j", "k",
                     "l", "ş", "i", "z", "x", "c", "v", "b", "n", "m", "ö", "ç"]
    buyuk_harfler = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "Ğ", "Ü", "A", "S", "D", "F", "G", "H", "J", "K",
                     "L", "Ş", "İ", "Z", "X", "C", "V", "B", "N", "M", "Ö", "Ç"]
    semboller = ["₺", "€", "$", "£", ">", "<", "$", "[", "]", "(", ")", "=", "?", "!", "/", "*", "-", "+", ":",
                 ".", ";", ",", "@", "~", "%"]

    # Seçili karakter setlerini belirle
    secili_karakterler = []
    if sayilar_var.get():
        secili_karakterler.extend(sayilar)
    if harfler_var.get():
        secili_karakterler.extend(kucuk_harfler + buyuk_harfler)
    if semboller_var.get():
        secili_karakterler.extend(semboller)

    # Hiçbir seçenek seçili değilse uyarı ver
    if not secili_karakterler:
        uyari_label.configure(text="En az bir seçenek seçilmelidir!")
        return

    sifre_uzunlugu = int(uzunluk_scale.get())
    if sifre_uzunlugu < 4:
        uyari_label.configure(text="Şifre uzunluğu en az 4 olmalı!")
        return

    uyari_label.configure(text="")

    # Şifreyi oluştur
    sifre = ''.join(random.choice(secili_karakterler) for _ in range(sifre_uzunlugu))

    textbox.delete(0, customtkinter.END)
    textbox.insert(customtkinter.END, sifre)


def temizle():
    """Textbox'ı temizler."""
    textbox.delete(0, customtkinter.END)


def uzunluk_guncelle(value):
    """Slider değeri değiştiğinde uzunluk etiketini günceller."""
    uzunluk_deger_label.configure(text=f"{int(value)} karakter")


def textbox_tikla(event):
    """Textbox'a tıklandığında metni seçer ve kopyalar."""
    textbox.select_range(0, customtkinter.END)
    textbox.icursor(customtkinter.END)
    if textbox.get():  # Eğer textbox boş değilse
        pyperclip.copy(textbox.get())
        kopyalandi_label.configure(text="✓ Kopyalandı!")
        # 2 saniye sonra etiketi temizle
        pyPassGenerator.after(2000, lambda: kopyalandi_label.configure(text=""))


# Ana pencere
pyPassGenerator = customtkinter.CTk()
pyPassGenerator.geometry("450x250")  # Yüksekliği biraz artırdım
pyPassGenerator.title("pyPassGenerator | Oktay ALA")
pyPassGenerator.resizable(False, False)

# Şifre uzunluğu
uzunluk_frame = customtkinter.CTkFrame(pyPassGenerator)
uzunluk_frame.pack(pady=10)
uzunluk_label = customtkinter.CTkLabel(uzunluk_frame, text="Şifre Uzunluğu:")
uzunluk_label.pack(side="left", padx=10)
uzunluk_scale = customtkinter.CTkSlider(uzunluk_frame, from_=4, to=32, command=uzunluk_guncelle)
uzunluk_scale.set(10)
uzunluk_scale.pack(side="left", padx=10)
uzunluk_deger_label = customtkinter.CTkLabel(uzunluk_frame, text="10 karakter")
uzunluk_deger_label.pack(side="left", padx=10)

# Uyarı etiketi
uyari_label = customtkinter.CTkLabel(pyPassGenerator, text="", text_color="red")
uyari_label.pack()

# Şifre kutusu - Genişliği artırıldı
textbox = customtkinter.CTkEntry(pyPassGenerator, width=400)
textbox.pack(pady=10)
textbox.bind('<Button-1>', textbox_tikla)  # Sol tık olayını bağla

# Checkbox
checkbox_frame = customtkinter.CTkFrame(pyPassGenerator)
checkbox_frame.pack(pady=10)
sayilar_var = customtkinter.BooleanVar(value=True)
harfler_var = customtkinter.BooleanVar(value=True)
semboller_var = customtkinter.BooleanVar(value=True)
sayilar_check = customtkinter.CTkCheckBox(checkbox_frame, text="Sayılar", variable=sayilar_var)
harfler_check = customtkinter.CTkCheckBox(checkbox_frame, text="Harfler", variable=harfler_var)
semboller_check = customtkinter.CTkCheckBox(checkbox_frame, text="Semboller", variable=semboller_var)
sayilar_check.pack(side="left", padx=10)
harfler_check.pack(side="left", padx=10)
semboller_check.pack(side="left", padx=10)

# Kopyalandı
kopyalandi_label = customtkinter.CTkLabel(pyPassGenerator, text="", text_color="green")
kopyalandi_label.pack()

# Butonlar
button_frame = customtkinter.CTkFrame(pyPassGenerator)
button_frame.pack(pady=10)
buton = customtkinter.CTkButton(button_frame, text="Oluştur", command=rastgelesifre, width=120)
buton.pack(side="left", padx=10)
temizlebuton = customtkinter.CTkButton(button_frame, text="Temizle", command=temizle, fg_color="tomato",hover_color="#D32F2F", width=120)
temizlebuton.pack(side="left", padx=10)


pyPassGenerator.mainloop()