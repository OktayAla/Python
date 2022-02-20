import tkinter as tk
from tkinter import *
import color_window_func

PyColor=tk.Tk()
PyColor.title("pyColor - Color Picker | Oktay ALA")
PyColor.geometry("370x310")
PyColor.configure()
PyColor.resizable(False, False)

#SARI#
saritext = tk.Label(text="Sarı")
saritext.place(x=5,y=10)

sari = tk.Button(command=color_window_func.sari1_class.sari1_func,bg="#FFFF00")
sari2 = tk.Button(command=color_window_func.sari2_class.sari2_func,bg="#BDB76B")
sari3 = tk.Button(command=color_window_func.sari3_class.sari3_func,bg="#F0E68C")
sari4 = tk.Button(command=color_window_func.sari4_class.sari4_func,bg="#EEE8AA")
sari5 = tk.Button(command=color_window_func.sari5_class.sari5_func,bg="#FFDAB9")
sari6 = tk.Button(command=color_window_func.sari6_class.sari6_func,bg="#FFE4B5")
sari7 = tk.Button(command=color_window_func.sari7_class.sari7_func,bg="#FFEFD5")
sari8 = tk.Button(command=color_window_func.sari8_class.sari8_func,bg="#FAFAD2")
sari9 = tk.Button(command=color_window_func.sari9_class.sari9_func,bg="#FFFACD")
sari10 = tk.Button(command=color_window_func.sari10_class.sari10_func,bg="#FFFFE0")

sari.place(x=70,y=10,width=20,height=20)
sari2.place(x=100,y=10,width=20,height=20)
sari3.place(x=130,y=10,width=20,height=20)
sari4.place(x=160,y=10,width=20,height=20)
sari5.place(x=190,y=10,width=20,height=20)
sari6.place(x=220,y=10,width=20,height=20)
sari7.place(x=250,y=10,width=20,height=20)
sari8.place(x=280,y=10,width=20,height=20)
sari9.place(x=310,y=10,width=20,height=20)
sari10.place(x=340,y=10,width=20,height=20)
############################################



#KIRMIZI#
kirmizitext = tk.Label(text="Kırmızı")
kirmizitext.place(x=5,y=40)

kirmizi = tk.Button(command=color_window_func.kirmizi1_class.kirmizi1_func,bg="#ff0000")
kirmizi2 = tk.Button(command=color_window_func.kirmizi2_class.kirmizi2_func,bg="#8B0000")
kirmizi3 = tk.Button(command=color_window_func.kirmizi3_class.kirmizi3_func,bg="#B22222")
kirmizi4 = tk.Button(command=color_window_func.kirmizi4_class.kirmizi4_func,bg="#DC143C")
kirmizi5 = tk.Button(command=color_window_func.kirmizi5_class.kirmizi5_func,bg="#CD5C5C")
kirmizi6 = tk.Button(command=color_window_func.kirmizi6_class.kirmizi6_func,bg="#F08080")
kirmizi7 = tk.Button(command=color_window_func.kirmizi7_class.kirmizi7_func,bg="#E9967A")
kirmizi8 = tk.Button(command=color_window_func.kirmizi8_class.kirmizi8_func,bg="#FA8072")
kirmizi9 = tk.Button(command=color_window_func.kirmizi9_class.kirmizi9_func,bg="#FFA07A")
kirmizi10 = tk.Button(command=color_window_func.kirmizi10_class.kirmizi10_func,bg="#FF9191")

kirmizi.place(x=70,y=40,width=20,height=20)
kirmizi2.place(x=100,y=40,width=20,height=20)
kirmizi3.place(x=130,y=40,width=20,height=20)
kirmizi4.place(x=160,y=40,width=20,height=20)
kirmizi5.place(x=190,y=40,width=20,height=20)
kirmizi6.place(x=220,y=40,width=20,height=20)
kirmizi7.place(x=250,y=40,width=20,height=20)
kirmizi8.place(x=280,y=40,width=20,height=20)
kirmizi9.place(x=310,y=40,width=20,height=20)
kirmizi10.place(x=340,y=40,width=20,height=20)
############################################



#YEŞİL#
yesiltext = tk.Label(text="Yeşil")
yesiltext.place(x=5,y=70)

yesil = tk.Button(command=color_window_func.yesil1_class.yesil1_func,bg="#00ff00")
yesil2 = tk.Button(command=color_window_func.yesil2_class.yesil2_func,bg="#006400")
yesil3 = tk.Button(command=color_window_func.yesil3_class.yesil3_func,bg="#228B22")
yesil4 = tk.Button(command=color_window_func.yesil4_class.yesil4_func,bg="#2E8B57")
yesil5 = tk.Button(command=color_window_func.yesil5_class.yesil5_func,bg="#3CB371")
yesil6 = tk.Button(command=color_window_func.yesil6_class.yesil6_func,bg="#5bc98c")
yesil7 = tk.Button(command=color_window_func.yesil7_class.yesil7_func,bg="#00FF7F")
yesil8 = tk.Button(command=color_window_func.yesil8_class.yesil8_func,bg="#00FA9A")
yesil9 = tk.Button(command=color_window_func.yesil9_class.yesil9_func,bg="#90EE90")
yesil10 = tk.Button(command=color_window_func.yesil10_class.yesil10_func,bg="#98FB98")

yesil.place(x=70,y=70,width=20,height=20)
yesil2.place(x=100,y=70,width=20,height=20)
yesil3.place(x=130,y=70,width=20,height=20)
yesil4.place(x=160,y=70,width=20,height=20)
yesil5.place(x=190,y=70,width=20,height=20)
yesil6.place(x=220,y=70,width=20,height=20)
yesil7.place(x=250,y=70,width=20,height=20)
yesil8.place(x=280,y=70,width=20,height=20)
yesil9.place(x=310,y=70,width=20,height=20)
yesil10.place(x=340,y=70,width=20,height=20)
############################################



#MAVİ#
mavitext = tk.Label(text="Mavi")
mavitext.place(x=5,y=100)

mavi = tk.Button(command=color_window_func.mavi1_class.mavi1_func,bg="#0000FF")
mavi2 = tk.Button(command=color_window_func.mavi2_class.mavi2_func,bg="#191970")
mavi3 = tk.Button(command=color_window_func.mavi3_class.mavi3_func,bg="#0000CD")
mavi4 = tk.Button(command=color_window_func.mavi4_class.mavi4_func,bg="#4169E1")
mavi5 = tk.Button(command=color_window_func.mavi5_class.mavi5_func,bg="#1E90FF")
mavi6 = tk.Button(command=color_window_func.mavi6_class.mavi6_func,bg="#87CEFA")
mavi7 = tk.Button(command=color_window_func.mavi7_class.mavi7_func,bg="#87CEEB")
mavi8 = tk.Button(command=color_window_func.mavi8_class.mavi8_func,bg="#ADD8E6")
mavi9 = tk.Button(command=color_window_func.mavi9_class.mavi9_func,bg="#B0E0E6")
mavi10 = tk.Button(command=color_window_func.mavi10_class.mavi10_func,bg="#E0FFFF")

mavi.place(x=70,y=100,width=20,height=20)
mavi2.place(x=100,y=100,width=20,height=20)
mavi3.place(x=130,y=100,width=20,height=20)
mavi4.place(x=160,y=100,width=20,height=20)
mavi5.place(x=190,y=100,width=20,height=20)
mavi6.place(x=220,y=100,width=20,height=20)
mavi7.place(x=250,y=100,width=20,height=20)
mavi8.place(x=280,y=100,width=20,height=20)
mavi9.place(x=310,y=100,width=20,height=20)
mavi10.place(x=340,y=100,width=20,height=20)
############################################



#TURUNCU#
turuncutext = tk.Label(text="Turuncu")
turuncutext.place(x=5,y=130)

turuncu = tk.Button(command=color_window_func.turuncu1_class.turuncu1_func,bg="#FFA500")
turuncu2 = tk.Button(command=color_window_func.turuncu2_class.turuncu2_func,bg="#61380B")
turuncu3 = tk.Button(command=color_window_func.turuncu3_class.turuncu3_func,bg="#8A4B08")
turuncu4 = tk.Button(command=color_window_func.turuncu4_class.turuncu4_func,bg="#B45F04")
turuncu5 = tk.Button(command=color_window_func.turuncu5_class.turuncu5_func,bg="#DF7401")
turuncu6 = tk.Button(command=color_window_func.turuncu6_class.turuncu6_func,bg="#FF8000")
turuncu7 = tk.Button(command=color_window_func.turuncu7_class.turuncu7_func,bg="#FE9A2E")
turuncu8 = tk.Button(command=color_window_func.turuncu8_class.turuncu8_func,bg="#FAAC58")
turuncu9 = tk.Button(command=color_window_func.turuncu9_class.turuncu9_func,bg="#F7BE81")
turuncu10 = tk.Button(command=color_window_func.turuncu10_class.turuncu10_func,bg="#F5D0A9")

turuncu.place(x=70,y=130,width=20,height=20)
turuncu2.place(x=100,y=130,width=20,height=20)
turuncu3.place(x=130,y=130,width=20,height=20)
turuncu4.place(x=160,y=130,width=20,height=20)
turuncu5.place(x=190,y=130,width=20,height=20)
turuncu6.place(x=220,y=130,width=20,height=20)
turuncu7.place(x=250,y=130,width=20,height=20)
turuncu8.place(x=280,y=130,width=20,height=20)
turuncu9.place(x=310,y=130,width=20,height=20)
turuncu10.place(x=340,y=130,width=20,height=20)
############################################



#MOR#
mortext = tk.Label(text="Mor")
mortext.place(x=5,y=160)

mor = tk.Button(command=color_window_func.mor1_class.mor1_func,bg="#800080")
mor2 = tk.Button(command=color_window_func.mor2_class.mor2_func,bg="#610B5E")
mor3 = tk.Button(command=color_window_func.mor3_class.mor3_func,bg="#8A0886")
mor4 = tk.Button(command=color_window_func.mor4_class.mor4_func,bg="#B404AE")
mor5 = tk.Button(command=color_window_func.mor5_class.mor5_func,bg="#DF01D7")
mor6 = tk.Button(command=color_window_func.mor6_class.mor6_func,bg="#FF00FF")
mor7 = tk.Button(command=color_window_func.mor7_class.mor7_func,bg="#FE2EF7")
mor8 = tk.Button(command=color_window_func.mor8_class.mor8_func,bg="#FA58F4")
mor9 = tk.Button(command=color_window_func.mor9_class.mor9_func,bg="#F781F3")
mor10 = tk.Button(command=color_window_func.mor10_class.mor10_func,bg="#F5A9F2")

mor.place(x=70,y=160,width=20,height=20)
mor2.place(x=100,y=160,width=20,height=20)
mor3.place(x=130,y=160,width=20,height=20)
mor4.place(x=160,y=160,width=20,height=20)
mor5.place(x=190,y=160,width=20,height=20)
mor6.place(x=220,y=160,width=20,height=20)
mor7.place(x=250,y=160,width=20,height=20)
mor8.place(x=280,y=160,width=20,height=20)
mor9.place(x=310,y=160,width=20,height=20)
mor10.place(x=340,y=160,width=20,height=20)
############################################



#KAHVERENGİ#
kahverengitext = tk.Label(text="Kahverengi")
kahverengitext.place(x=5,y=190)

kahverengi = tk.Button(command=color_window_func.kahverengi1_class.kahverengi1_func,bg="#A52A2A")
kahverengi2 = tk.Button(command=color_window_func.kahverengi2_class.kahverengi2_func,bg="#800000")
kahverengi3 = tk.Button(command=color_window_func.kahverengi3_class.kahverengi3_func,bg="#8B4513")
kahverengi4 = tk.Button(command=color_window_func.kahverengi4_class.kahverengi4_func,bg="#A0522D")
kahverengi5 = tk.Button(command=color_window_func.kahverengi5_class.kahverengi5_func,bg="#D2691E")
kahverengi6 = tk.Button(command=color_window_func.kahverengi6_class.kahverengi6_func,bg="#CD853F")
kahverengi7 = tk.Button(command=color_window_func.kahverengi7_class.kahverengi7_func,bg="#F4A460")
kahverengi8 = tk.Button(command=color_window_func.kahverengi8_class.kahverengi8_func,bg="#DEB887")
kahverengi9 = tk.Button(command=color_window_func.kahverengi9_class.kahverengi9_func,bg="#F5DEB3")
kahverengi10 = tk.Button(command=color_window_func.kahverengi10_class.kahverengi10_func,bg="#FFE4C4")

kahverengi.place(x=70,y=190,width=20,height=20)
kahverengi2.place(x=100,y=190,width=20,height=20)
kahverengi3.place(x=130,y=190,width=20,height=20)
kahverengi4.place(x=160,y=190,width=20,height=20)
kahverengi5.place(x=190,y=190,width=20,height=20)
kahverengi6.place(x=220,y=190,width=20,height=20)
kahverengi7.place(x=250,y=190,width=20,height=20)
kahverengi8.place(x=280,y=190,width=20,height=20)
kahverengi9.place(x=310,y=190,width=20,height=20)
kahverengi10.place(x=340,y=190,width=20,height=20)
############################################



#PEMBE#
pembetext = tk.Label(text="Pembe")
pembetext.place(x=5,y=220)

pembe = tk.Button(command=color_window_func.pembe1_class.pembe1_func,bg="#FFC0CB")
pembe2 = tk.Button(command=color_window_func.pembe2_class.pembe2_func,bg="#610B4B")
pembe3 = tk.Button(command=color_window_func.pembe3_class.pembe3_func,bg="#8A0868")
pembe4 = tk.Button(command=color_window_func.pembe4_class.pembe4_func,bg="#B40486")
pembe5 = tk.Button(command=color_window_func.pembe5_class.pembe5_func,bg="#DF01A5")
pembe6 = tk.Button(command=color_window_func.pembe6_class.pembe6_func,bg="#C71585")
pembe7 = tk.Button(command=color_window_func.pembe7_class.pembe7_func,bg="#FF1493")
pembe8 = tk.Button(command=color_window_func.pembe8_class.pembe8_func,bg="#FF69B4")
pembe9 = tk.Button(command=color_window_func.pembe9_class.pembe9_func,bg="#DB7093")
pembe10 = tk.Button(command=color_window_func.pembe10_class.pembe10_func,bg="#FFB6C1")

pembe.place(x=70,y=220,width=20,height=20)
pembe2.place(x=100,y=220,width=20,height=20)
pembe3.place(x=130,y=220,width=20,height=20)
pembe4.place(x=160,y=220,width=20,height=20)
pembe5.place(x=190,y=220,width=20,height=20)
pembe6.place(x=220,y=220,width=20,height=20)
pembe7.place(x=250,y=220,width=20,height=20)
pembe8.place(x=280,y=220,width=20,height=20)
pembe9.place(x=310,y=220,width=20,height=20)
pembe10.place(x=340,y=220,width=20,height=20)
############################################



#SİYAH#
siyahtext = tk.Label(text="Siyah")
siyahtext.place(x=5,y=250)

siyah = tk.Button(command=color_window_func.siyah1_class.siyah1_func,bg="#000000")
siyah2 = tk.Button(command=color_window_func.siyah2_class.siyah2_func,bg="#151515")
siyah3 = tk.Button(command=color_window_func.siyah3_class.siyah3_func,bg="#1C1C1C")
siyah4 = tk.Button(command=color_window_func.siyah4_class.siyah4_func,bg="#2E2E2E")
siyah5 = tk.Button(command=color_window_func.siyah5_class.siyah5_func,bg="#424242")
siyah6 = tk.Button(command=color_window_func.siyah6_class.siyah6_func,bg="#585858")
siyah7 = tk.Button(command=color_window_func.siyah7_class.siyah7_func,bg="#6E6E6E")
siyah8 = tk.Button(command=color_window_func.siyah8_class.siyah8_func,bg="#848484")
siyah9 = tk.Button(command=color_window_func.siyah9_class.siyah9_func,bg="#A4A4A4")
siyah10 = tk.Button(command=color_window_func.siyah10_class.siyah10_func,bg="#BDBDBD")

siyah.place(x=70,y=250,width=20,height=20)
siyah2.place(x=100,y=250,width=20,height=20)
siyah3.place(x=130,y=250,width=20,height=20)
siyah4.place(x=160,y=250,width=20,height=20)
siyah5.place(x=190,y=250,width=20,height=20)
siyah6.place(x=220,y=250,width=20,height=20)
siyah7.place(x=250,y=250,width=20,height=20)
siyah8.place(x=280,y=250,width=20,height=20)
siyah9.place(x=310,y=250,width=20,height=20)
siyah10.place(x=340,y=250,width=20,height=20)
############################################



#BEYAZ#
beyaztext = tk.Label(text="Beyaz")
beyaztext.place(x=5,y=280)

beyaz = tk.Button(command=color_window_func.beyaz1_class.beyaz1_func,bg="#FFFFFF")
beyaz2 = tk.Button(command=color_window_func.beyaz2_class.beyaz2_func,bg="#FFFAFA")
beyaz3 = tk.Button(command=color_window_func.beyaz3_class.beyaz3_func,bg="#F5FFFA")
beyaz4 = tk.Button(command=color_window_func.beyaz4_class.beyaz4_func,bg="#F0FFFF")
beyaz5 = tk.Button(command=color_window_func.beyaz5_class.beyaz5_func,bg="#F0F8FF")
beyaz6 = tk.Button(command=color_window_func.beyaz6_class.beyaz6_func,bg="#F8F8FF")
beyaz7 = tk.Button(command=color_window_func.beyaz7_class.beyaz7_func,bg="#F5F5F5")
beyaz8 = tk.Button(command=color_window_func.beyaz8_class.beyaz8_func,bg="#FFF0F5")
beyaz9 = tk.Button(command=color_window_func.beyaz9_class.beyaz9_func,bg="#FFF5EE")
beyaz10 = tk.Button(command=color_window_func.beyaz10_class.beyaz10_func,bg="#FFFFF0")

beyaz.place(x=70,y=280,width=20,height=20)
beyaz2.place(x=100,y=280,width=20,height=20)
beyaz3.place(x=130,y=280,width=20,height=20)
beyaz4.place(x=160,y=280,width=20,height=20)
beyaz5.place(x=190,y=280,width=20,height=20)
beyaz6.place(x=220,y=280,width=20,height=20)
beyaz7.place(x=250,y=280,width=20,height=20)
beyaz8.place(x=280,y=280,width=20,height=20)
beyaz9.place(x=310,y=280,width=20,height=20)
beyaz10.place(x=340,y=280,width=20,height=20)
############################################


PyColor.mainloop()