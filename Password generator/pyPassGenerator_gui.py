import customtkinter
import random

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

def rastgelesifre():
    """Rastgele şifre oluşturur ve textbox'a yazdırır."""
    sayilar = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    kucuk_harfler = ["q", "w", "e", "r", "t", "y", "u", "ı", "o", "p", "ğ", "ü", "a", "s", "d", "f", "g", "h", "j", "k", "l", "ş", "i", "z", "x", "c", "v", "b", "n", "m", "ö", "ç"]
    buyuk_harfler = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "Ğ", "Ü", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Ş", "İ", "Z", "X", "C", "V", "B", "N", "M", "Ö", "Ç"]
    semboller = ["₺", "€", "$", "£", ">", "<", "$", "½", "[", "]", "(", ")", "=", "?", "!", "/", "*", "-", "+", ":", ".", ";", ",", "@", "ß", "~", "%"]

    karakterler = sayilar + kucuk_harfler + buyuk_harfler + semboller

    sifre_uzunlugu = int(uzunluk_scale.get())
    if sifre_uzunlugu < 4:
        uyari_label.configure(text="Şifre uzunluğu en az 4 olmalı!")
        return
    else:
        uyari_label.configure(text="")

    rastgele_karakterler = random.choice(sayilar) + random.choice(kucuk_harfler) + random.choice(buyuk_harfler) + random.choice(semboller)

    for _ in range(sifre_uzunlugu - 4):
        rastgele_karakterler += random.choice(karakterler)

    rastgele_karakterler_liste = list(rastgele_karakterler)
    random.shuffle(rastgele_karakterler_liste)

    sifre = ''.join(rastgele_karakterler_liste)
    textbox.delete(0, customtkinter.END)
    textbox.insert(customtkinter.END, sifre)

def temizle():
    """Textbox'ı temizler."""
    textbox.delete(0, customtkinter.END)

# Ana pencere
pyPassGenerator = customtkinter.CTk()
pyPassGenerator.geometry("450x220")  # Boyutları biraz daha artırdım
pyPassGenerator.title("pyPassGenerator | Oktay ALA")
pyPassGenerator.resizable(False, False)  # Yeniden boyutlandırmayı kapattım

# Şifre uzunluğu
uzunluk_frame = customtkinter.CTkFrame(pyPassGenerator)  # Frame ekledim
uzunluk_frame.pack(pady=20)  # Üstten ve alttan boşluk

uzunluk_label = customtkinter.CTkLabel(uzunluk_frame, text="Şifre Uzunluğu:")
uzunluk_label.pack(side="left", padx=10)

uzunluk_scale = customtkinter.CTkSlider(uzunluk_frame, from_=4, to=32)
uzunluk_scale.set(10)
uzunluk_scale.pack(side="left", padx=10)

# Uyarı etiketi
uyari_label = customtkinter.CTkLabel(pyPassGenerator, text="", text_color="red")
uyari_label.pack()

# Şifre kutusu
textbox = customtkinter.CTkEntry(pyPassGenerator, width=300)  # Genişliği artırdım
textbox.pack(pady=10)

# Butonlar
button_frame = customtkinter.CTkFrame(pyPassGenerator)  # Butonlar için frame
button_frame.pack(pady=10)

buton = customtkinter.CTkButton(button_frame, text="Oluştur", command=rastgelesifre, width=120)  # Genişlik belirttim
buton.pack(side="left", padx=10)

temizlebuton = customtkinter.CTkButton(button_frame, text="Temizle", command=temizle, fg_color="tomato", hover_color="#D32F2F", width=120)  # Genişlik belirttim
temizlebuton.pack(side="left", padx=10)

pyPassGenerator.mainloop()