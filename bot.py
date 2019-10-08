import tweepy
import time
import requests
import urllib.parse
import random
from bs4 import BeautifulSoup



def rockko():

    rock=''
    sert=["a","o","u","ı"]
    sertis=["o","u"]

    yum =["e","ö","ü","i"]
    yumis =["ö", "ü"]

    #random zar atici
    zar = random.randint(1, 100)
    if zar>44:
        zarval=3
    elif zar>10 and zar<45:
        zarval=2
    else:
        zarval=1


    #kelime alici ve birlestirici
    for i in range(zarval):
        url = 'https://www.nisanyansozluk.com/?k=Allah'
        r = requests.get(url)
        text= r.text
        #Hep buradan basliyor ve random kelime buluyor asagidan
        hdata= open("htmldata.txt","w+")
        hdata.write(str(r.text.encode("utf-8")))

        soup = BeautifulSoup(text, "html.parser")
        alar = (soup.find_all('a'))
        #html koddan a href kodlulari ayirdik
        kelime = (soup.title.string)
        kelime = kelime.split()
        kelime = kelime[0]

        #49.a'da random kelimenin kodu var onu aldik cevirdik, htmlde kod bozuluyo urllible duzelttik
        rankel= alar[49]
        rankel=str(rankel)
        rankel=rankel.split('"')
        rankel=rankel[1]
        rankel=str(rankel)
        kelime = urllib.parse.unquote(rankel[3:])
        kelime =str(kelime)
        kelime = kelime.capitalize()


        #bazi kelimelerin sonunda - var onu silip ek eklemek lazim (yig-, sayili olanlar var, hav2, tok1 gibi), (o)+'lular var, ufal-), yüz-2
        #dilbilgili bir ek eklemece olmasi lazim
        #once suffa attigimiz seylere baksin ve onlari silsin
        suff=["(o)+", "-1", "-2", "1", "2", "-", "4", "5", "3"]
        suffnum=0
        #once kac kelimelik bi isim yapiyoz ona bakalim ona gore silelim ve editleyelim

        for j in suff:
            if j in kelime:
                lenkel = len(j)
                kelime = kelime[:len(kelime) - lenkel]
            else:
                suffnum=suffnum+1

        #simdi suffnum bize suffdan hangisine sahip oldugunu soylicek 9 ise hic biri, buyuk unlu uyumuna da bakmamiz lazm simdi

        if kelime[-1] in sert:
                coguleki="lar"

        elif kelime[-1] in yum:
            coguleki="ler"


        elif kelime[-2] in sert:
            coguleki="lar"

        elif kelime[-2] in yum:
            coguleki="ler"


        elif kelime[-3] in sert:
            coguleki="lar"


        elif kelime[-3] in yum:
            coguleki="ler"


        #simdi kelime sayisina gore ekler ekleyek farklilastirici

        if zarval == 1:
            zar2=random.randint(1, 20)
            if zar2 > 14:
                kelime=kelime+coguleki
                rock= kelime
            elif zar2 <4:
                rock="Grup "+kelime
            else:
                rock=kelime

        elif zarval == 2:
            zar2 = random.randint(1, 20)
            if zar2 > 18:
               if i == 0:
                   kelime=kelime+coguleki
            elif zar2 < 2:
                if i == 1:
                    kelime=kelime+coguleki
            rock = rock + " " + kelime

        elif zarval == 3:
            zar2 = random.randint(1, 20)
            if zar2 > 19:
                if i == 2:
                    kelime=kelime+coguleki
                rock = rock + " " + kelime

            elif zar2 < 3:
                if i == 0:
                    kelime=kelime

                rock = rock + " " + kelime
            else:
                rock = rock + " " + kelime
        hdata.close


    return rock

# Authenticate to Twitter
auth = tweepy.OAuthHandler("0UynTKJuReVMYKAcnv4hJolgs",
    "hgd9JKvcMyjm3DLzeIPF7ohwLe6MfNbukGRvGfLAckKyvLGqEA")
auth.set_access_token("1181690002524127232-DVCl6epN68ICq7MwEf68Uwo7Yi0gdt",
    "i1L073pN7YBZdJbfHXcn6yexkg3S4LVZtJXZJqlhbf0yk")

api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)
api.verify_credentials()
print("Authentication OK")
counter = 1
while True:
    api.update_status(rockko(), counter)
    counter += 1
    time.sleep(1800)
