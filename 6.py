#sada već ulazimo u malo dublje vode :D
#sada ćemo se malo zabaviti rječnicima (dictionary)
#to je vrsta podatka jako slična nizovima, ali radi sa ključevima i indeksima
#svakoj vrijednosti unutar rječnika možemo pristupiti korištenjem ključa

#rječnik pravimo koristeći {}
#hajde da napravimo imenik sa brojevima telefona

imenik = {}

imenik["Selma"] = 123456789
imenik["Cicko"] = 987654321
imenik["Bajro"] = 135798642
imenik["Mukelefeta"] = 246897531

#u ovom slučaju "Selma" je ključ, a broj je vrijednost i mi preko ključa možemo dobiti broj/vrijednost

print(imenik["Selma"])
#rječnici se mogu pisati i na sljedeći način (ali ovaj iznad način je češći)

imenik1 = {
    "Fata": 623478,
    "Huso": 634568,
    "Hasiba": 645680,
    "Mujaga": 656791,
    "Zehra": 668912
}

print(imenik1)

#iteracija(ponavljanje) pomoću petlje je moguće uraditi nad rječnicima

for ime, broj in imenik1.items():
    print("%s ima telefonski broj %d" %(ime, broj))

#items() je metoda rječnika koja vraća sve parove (ključ, vrijednost) iz tog rječnika


#uz sve navedeno, baš kao u pravom rječniku.. ili bolje reći imeniku.. postoji mogućnost brisanja podataka
#dovoljno je samo iskoristiti ljučnu riječ del i navesti šta tačno želimo da izbrišemo

#del imenik1["Mujaga"]
#odkomentariši i kompajliraj ako želiš da izbrišeš jadnog Mujagu ;(
#drugi način brisanja:
#imenik1.pop["Mujaga"]
#------------------------------------------------------------------------------------------------------------------------
#moduli i paketi

#u programiranju, moduli su posebni "komadići" sofwera koji imaju posebnu funkcionalnost
#svaki modul se sastoji od različitih fajlova koji se mogu editovati odvojeno
#moduli u pythonu su samo fajlovi sa .py ekstenzijom

#Python modul može imati skup definiranih i implementiranih funkcija, klasa ili varijabli.

#zamislimo da imamo projek gdje želimo da napravimo neku igricu
# Imamo dva Python fajla: game.py i draw.py
# 
# draw.py sadrži funkciju draw_game(), koja je zadužena za crtanje igre.
# game.py je glavni fajl koji pokreće igru. U njemu koristimo ključnu riječ "import"
# da bismo uključili funkcije iz draw.py, odnosno uključujemo cijeli taj modul.
# Kada napišemo "import draw" u game.py, mi zapravo učitavamo draw.py fajl kao modul.

#ja nemam sada neke kreirane module za vježbu, ali ovo bi bila sintaksa
#import draw

#print(help("modules"))
#preko ove linije koda iznad se mogu vidjeti svi dostupni 
#print(help("math"))
#npr. ovako možemo vidjeti šta "math" modul nudi
import math 
#i sada možemo koristiti modul math
#i recimo da sada želimo vrijednost od pi
print(math.pi)

# mogu se davati i alijasi modulima tipa import math as m
#ako želimo nešto specifično iz modula, može se koristiti sljedeće
#from math import pi

#-----------------------------------------------------------------------------------
#paketi
#paketi (packages) sadrže više modula, a biblioteke sadrže više modula i paketa
#jedno od pravila je da paketi MORAJU  u svom direktoriju (folderu) imaju poseban fajl __init__.py
#__init__.py može biti i prazan fajl, ali on MORA postojati
#to mora biti tako jer baš ovaj fajl pokazuje da je ovo u pitanju python paket
#npr napravimo direktorij sa imenom matematika i u njemu modul linearna, da bi koristili taj modul, pišemo
# import matematika.linearna
#može i from matematika import linearna
#hijerarhija biblioteka, paketa i modula je prikazana na slici 1

#baš kao što smo pristupili modulu math, postoje i biblioteke i paketi kojima se može tako pristupiti
import matplotlib.backends.backend_pdf # type: ignore
#biblioteka -> paket -> modul
