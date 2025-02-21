import tkinter as tk
from tkinter import *
import colorsys

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_cmyk(rgb_color):
    r, g, b = [x / 255 for x in rgb_color]
    k = 1 - max(r, g, b)
    if k == 1:
        return 0, 0, 0, 1
    c = (1 - r - k) / (1 - k)
    m = (1 - g - k) / (1 - k)
    y = (1 - b - k) / (1 - k)
    return c, m, y, k

def renk_parlakligi(hex_color):
    rgb = hex_to_rgb(hex_color)
    # BT.709 standardına göre parlaklık hesaplama
    return (0.2126 * rgb[0] + 0.7152 * rgb[1] + 0.0722 * rgb[2])

def renk_bilgisi_popup(renk_kodu):
    rgb = hex_to_rgb(renk_kodu)
    cmyk = rgb_to_cmyk(rgb)
    hsv = colorsys.rgb_to_hsv(rgb[0] / 255, rgb[1] / 255, rgb[2] / 255)
    hsl = colorsys.rgb_to_hls(rgb[0] / 255, rgb[1] / 255, rgb[2] / 255)

    popup = tk.Toplevel()
    popup.title("Renk Bilgisi")
    popup.geometry("250x150")
    popup.configure(bg=renk_kodu)

    parlaklik = renk_parlakligi(renk_kodu)
    metin_rengi = "black" if parlaklik > 128 else "white"  # Eşik değeri ayarlanabilir

    tk.Label(popup, text="HEX Kodu:", bg=renk_kodu, fg=metin_rengi).grid(row=0, column=0, sticky="w", padx=5, pady=2)
    hex_text = tk.Entry(popup)
    hex_text.insert(0, renk_kodu)
    hex_text.config(state="readonly")  # Sadece okunabilir yap
    hex_text.grid(row=0, column=1, sticky="ew", padx=5, pady=2)

    tk.Label(popup, text="RGB Değeri:", bg=renk_kodu, fg=metin_rengi).grid(row=1, column=0, sticky="w", padx=5, pady=2)
    rgb_text = tk.Entry(popup)
    rgb_text.insert(0, str(rgb))
    rgb_text.config(state="readonly")
    rgb_text.grid(row=1, column=1, sticky="ew", padx=5, pady=2)

    tk.Label(popup, text="CMYK Değeri:", bg=renk_kodu, fg=metin_rengi).grid(row=2, column=0, sticky="w", padx=5, pady=2)
    cmyk_text = tk.Entry(popup)
    cmyk_text.insert(0, str(tuple(round(x, 2) for x in cmyk)))  # Yuvarla ve tuple yap
    cmyk_text.config(state="readonly")
    cmyk_text.grid(row=2, column=1, sticky="ew", padx=5, pady=2)

    tk.Label(popup, text="HSV Değeri:", bg=renk_kodu, fg=metin_rengi).grid(row=3, column=0, sticky="w", padx=5, pady=2)
    hsv_text = tk.Entry(popup)
    hsv_text.insert(0, str(tuple(round(x, 2) for x in hsv)))
    hsv_text.config(state="readonly")
    hsv_text.grid(row=3, column=1, sticky="ew", padx=5, pady=2)

    tk.Label(popup, text="HSL Değeri:", bg=renk_kodu, fg=metin_rengi).grid(row=4, column=0, sticky="w", padx=5, pady=2)
    hsl_text = tk.Entry(popup)
    hsl_text.insert(0, str(tuple(round(x, 2) for x in hsl)))
    hsl_text.config(state="readonly")
    hsl_text.grid(row=4, column=1, sticky="ew", padx=5, pady=2)

def renk_dugmesi_olustur(renk_kodu):
    komut = lambda c=renk_kodu: renk_bilgisi_popup(c)  # Renk kodunu lambda ile yakala
    dugme = tk.Button(bg=renk_kodu, command=komut, width=2, height=1)
    return dugme

# Renkler
renkler = {
    "Sarı": [
        ("#FFFF00"),
        ("#BDB76B"),
        ("#F0E68C"),
        ("#EEE8AA"),
        ("#FFDAB9"),
        ("#FFE4B5"),
        ("#FFEFD5"),
        ("#FAFAD2"),
        ("#FFFACD"),
        ("#FFFFE0"),
    ],
    "Kırmızı": [
        ("#ff0000"),
        ("#8B0000"),
        ("#B22222"),
        ("#DC143C"),
        ("#CD5C5C"),
        ("#F08080"),
        ("#E9967A"),
        ("#FA8072"),
        ("#FFA07A"),
        ("#FF9191"),
    ],
    "Yeşil": [
        ("#00ff00"),
        ("#006400"),
        ("#228B22"),
        ("#2E8B57"),
        ("#3CB371"),
        ("#5bc98c"),
        ("#00FF7F"),
        ("#00FA9A"),
        ("#90EE90"),
        ("#98FB98"),
    ],
    "Mavi": [
        ("#0000FF"),
        ("#191970"),
        ("#0000CD"),
        ("#4169E1"),
        ("#1E90FF"),
        ("#87CEFA"),
        ("#87CEEB"),
        ("#ADD8E6"),
        ("#B0E0E6"),
        ("#E0FFFF"),
    ],
    "Turuncu": [
        ("#FFA500"),
        ("#61380B"),
        ("#8A4B08"),
        ("#B45F04"),
        ("#DF7401"),
        ("#FF8000"),
        ("#FE9A2E"),
        ("#FAAC58"),
        ("#F7BE81"),
        ("#F5D0A9"),
    ],
    "Mor": [
        ("#800080"),
        ("#610B5E"),
        ("#8A0886"),
        ("#B404AE"),
        ("#DF01D7"),
        ("#FF00FF"),
        ("#FE2EF7"),
        ("#FA58F4"),
        ("#F781F3"),
        ("#F5A9F2"),
    ],
    "Kahverengi": [
        ("#A52A2A"),
        ("#800000"),
        ("#8B4513"),
        ("#A0522D"),
        ("#D2691E"),
        ("#CD853F"),
        ("#F4A460"),
        ("#DEB887"),
        ("#F5DEB3"),
        ("#FFE4C4"),
    ],
    "Pembe": [
        ("#FFC0CB"),
        ("#610B4B"),
        ("#8A0868"),
        ("#B40486"),
        ("#DF01A5"),
        ("#C71585"),
        ("#FF1493"),
        ("#FF69B4"),
        ("#DB7093"),
        ("#FFB6C1"),
    ],
    "Siyah": [
        ("#000000"),
        ("#151515"),
        ("#1C1C1C"),
        ("#2E2E2E"),
        ("#424242"),
        ("#585858"),
        ("#6E6E6E"),
        ("#848484"),
        ("#A4A4A4"),
        ("#BDBDBD"),
    ],
    "Beyaz": [
        ("#FFFFFF"),
        ("#FFFAFA"),
        ("#F5FFFA"),
        ("#F0FFFF"),
        ("#F0F8FF"),
        ("#F8F8FF"),
        ("#F5F5F5"),
        ("#FFF0F5"),
        ("#FFF5EE"),
        ("#FFFFF0"),
    ],
}

PyColor = tk.Tk()
PyColor.title("pyColor - Color Picker | Oktay ALA")
PyColor.geometry("370x310")
PyColor.configure()
PyColor.resizable(False, False)

# Renkleri ve düğmeleri oluşturma
satir = 0
for renk_adi, renk_tonlari in renkler.items():
    # Renk etiketi
    renk_etiketi = tk.Label(text=renk_adi)
    renk_etiketi.grid(row=satir, column=0, padx=5, pady=5, sticky="w")

    # Renk düğmeleri
    for i, (renk_kodu) in enumerate(renk_tonlari):
        dugme = renk_dugmesi_olustur(renk_kodu)
        dugme.grid(row=satir, column=i + 1, padx=2, pady=2)

    satir += 1

PyColor.mainloop()