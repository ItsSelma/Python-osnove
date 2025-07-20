#kako bi ispisali početni tekst, koristit ćemo print()
print("Zdravo Nevesinje moje, zdravo o mila grudo!")
#jednom kada kompajlamo kod, vidjet ćemo ispis u terminalu
#u pythonu ne postoje zagrade u klasičnom smislu kao što smo se navikli u npr. c# ili c++ "{}"
#umjesto toga, python koristi nešto što se zove uvlačenje
#uvlačenje je, najjednostavnije pojašnjeno, gomila razmaka
#u ovom slučaju 4 razmaka
#može se koristiti i dugme "tab"

x = 1 #ovako definisemo varijablu
if x == 1:              #već usput vidimo definisanje if uslova, ne vidimo zagrade, ali se ovo ponaša kao if(x==1){}
    print("X ima vrijednost 1")


#to je to pametovanja oko printa i uvlacenja :D, hajdemo sada na brojeve i varijable

#python koristi 2 tipa brojeva, a to su integer i float
#da bi definirali integer, dovoljno je da navedemo cjelobrojnu vrijednost (1, 2, 3, 4)

mojInt = 1
print(mojInt)

#za definiranje float-a (3.495, 24.5, 6.347552) postoje 2 notacije koje možemo koristiti

#prva
mojFloat = 4.0   #ovime smo rekli da se ne radi o cjelobrojnom broju
print(mojFloat)
#drugi nacin

mojFloat1 = float(5) #vidimo da iako nismo naglasili decimalni zarez da ponovo dobijamo ispis "5.0"
print(mojFloat1)

#e hajde sada malo o stringovima
#stringovi se mogu naznačiti sa "" ili ''

mojString = "Hejjjj"
print(mojString)

mojString = 'Caoo'
print(mojString)
# primjecujemo kako je jedna vrijednost "pregazila" drugu u ovoj varijabli

# u kodu ne paravi razliku "" i '', ali je ipak bolje koristiti "" ako pišemo na engleskom
#primjer :

apostrofi = "Don't you dare!"
print(apostrofi)

# eh, sada kada smo odradili osnovno gradivo za brojeve i stringove, hajmo malo vidjeti operatore vezane za njih

#imamo klasične operatore koje smo i prije susretali u životu, hajde da vidimo za npr +

jedan = 1
dva = 2
tri = jedan + dva
print(tri)


zdravo = "zdravo"
svijete = "svijete"
pozdrav = zdravo + " " + svijete
print(pozdrav)

#također, dodjelu varijabli možemo izvršiti u jednom redu na sljedeći način:

a, b = 3, 4
print(a, b)  #vidimo kako print dozvoljava pisanje više varijabli unutar istog printa

#ako miješamo stringove i brojeve, doci ce do greške jer mu neće biti jasno je li u pitanju računanje brojeva ili pisanje stringa

# jedan1 = 1
# dva2 = 2

# zdravo1 = "zdravo"
# print(jedan1 + dva2 + zdravo1)

#zakomentarisano radi errora, odkomentarisati po potrebi (Ctrl + K, pa Ctrl + U)

#----------------------------------------------------------------------------------------------
#vrijeme je da idemo na liste!

#liste su skoro iste kao i nizovi, evo kako pravimo listu

mojaLista = []
mojaLista.append(1)  #dodajemo 1 na poziciju 0 tj. početak liste
mojaLista.append(2) #dodajemo 2 na poziciju 1
mojaLista.append(3) #dodajemo 3 na poziciju 2...

#sada možemo printati 
print(mojaLista[0])
print(mojaLista[1])
print(mojaLista[2])

#možemo napisati elemente liste i u jednom printu pomoću for petlje

for i in mojaLista:
    print(i)

#naravno, ako pokušamo da pristupimo indexu u listi (elementu) koji ne postoji, dobit ćemo error

#print(mojaLista[6])