import random
import array

max_karakter = 10

sayilar = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

kucuk_harfler = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                 't', 'u', 'v', 'w', 'x', 'y', 'z']

buyuk_harfler = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

semboller = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']

karakterler = sayilar + kucuk_harfler + buyuk_harfler + semboller

rastgele_sayilar = random.choice(sayilar)
rastgele_kucuk_harfler = random.choice(kucuk_harfler)
rastgele_buyuk_harfler = random.choice(buyuk_harfler)
rastgele_semboller = random.choice(semboller)

rastgele_karakterler = rastgele_sayilar + rastgele_kucuk_harfler + \
                       rastgele_buyuk_harfler + rastgele_semboller

for x in range(max_karakter - 4):
    rastgele_karakterler = rastgele_karakterler + random.choice(karakterler)

    rastgele_karakterler_liste = array.array('u', rastgele_karakterler)
    random.shuffle(rastgele_karakterler_liste)

sifre = ""
for x in rastgele_karakterler_liste:
    sifre = sifre + x

print(sifre)