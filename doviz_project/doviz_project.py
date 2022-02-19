import requests
from bs4 import BeautifulSoup

USDhtml = requests.get("https://finanswebde.com/doviz/USD")
USDsoup = BeautifulSoup(USDhtml.content,features = "lxml")
USDtag = USDsoup.findAll("nobr")

USDsayac = 0
for USD in USDtag:
    USD_Yazdir = USD.text
    print("USD/TRY:",USD_Yazdir)
    USDsayac += 1
    if USDsayac == 1:
        break


EURhtml = requests.get("https://finanswebde.com/doviz/EUR")
EURsoup = BeautifulSoup(EURhtml.content,features = "lxml")
EURtag = EURsoup.findAll("nobr")

EURsayac = 0
for EUR in EURtag:
    EUR_Yazdir = EUR.text
    print("EUR/TRY:",EUR_Yazdir)
    EURsayac += 1
    if EURsayac == 1:
        break


GBPhtml = requests.get("https://finanswebde.com/doviz/GBP")
GBPsoup = BeautifulSoup(GBPhtml.content,features = "lxml")
GBPtag = GBPsoup.findAll("nobr")

GBPsayac = 0
for GBP in GBPtag:
    GBP_Yazdir = GBP.text
    print("GBP/TRY:",GBP_Yazdir)
    GBPsayac += 1
    if GBPsayac == 1:
        break

