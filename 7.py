#inputi i outputi
#input funkcija je jedna jako korisna funkcija koja omogućava unos korisniku naše aplikacije
#možemo input sačuvati u neku varijablu i koristiti je za razne potrebe aplikacije
print("Unesite svoje ime")
varijabla = input()
print("Zdravo, %s!" %(varijabla))

#kada korisnik unese podatak, moguće je konvertovanje u razne vrste podataka

print("unesite broj")
broj = int(input())
print("Vaš broj je %d" %(broj))

#postoji funkcija map() koja služi da navedemo šta želimo da se odradi nad nizom elemenata
#recimo da želimo da napišemo da korisnik može unijeti dva elementa i da mi ta dva elementa odmah pretvorimo u integer
print("unesite dva broja")
a, b = map(int, input().split())
print("vaša dva broja su %d i %d" %(a,b))

#output formatting, tj izlazno formatiranje
#njega smo tehnički već prešli jer vidimo kak odobivamo preko printa ispis onoga što korisnik unese
#također u inputu možemo pisati natuknice za korisnike aplikacije

prezime =str(input("Unesite svoje prezime: "))
print("Vaše prezime je %s" %(prezime))
#str() je funkcija koja pretvara vrijednost u string

#--------------------------------------------------------------------------------------------
#generatori
#generatori su vrsta iteratora samo sa drugačijim pristupom
#neku funkciju pretvaramo u generator sa ključnom riječi "yield"

import random

def lutrija():
    for i in range(5):
        yield random.randint(1, 100)

for rando in lutrija():
    print("Vaš broj je %d" %(rando))


#-----------------------------------------------------------------------------------------------------------------------------

#List Comprehensions

#List Comprehensions je alat koji služi za kreiranje liste, na osnovu druge liste u jednoj, čitljivoj liniji
#za razumjevanje odradit ćemo dva primjera
#prvo hajde da napravimo novu listu gdje se računa veličina riječi iz predhodne liste, ali sa izbacivanjem riječi "danas"

recenica = "Danas je lijep dan"
rijeci = recenica.split()
rijeci_duzina = []

for rj in rijeci:
    if rj != "Danas":
        rijeci_duzina.append(len(rj))

print(rijeci)
print(rijeci_duzina)

#još jedan primjer.. koji je možda približniji "List Comprehensions" ideji jer je više optimizovano je sljedeći 

brojj = [1, 2, 3,4,5,6,7,8,9,10,11,12,13,14,15]

parniBrojevi = [bro for bro in brojj if bro%2 == 0]

print(parniBrojevi)

#-----------------------------------------------------------------------------------------------------------------------
#Lambda funkcije

#lambda funkcije se većinom koriste kada znamo da nam ta funkcija neće više trebati nego možda za 1 slučaj
#one su anonimne funkcije što znači da nemaju svoje ime

#koristi se ključna riječ "lambda"
#navedemo  parametar ili parametre koji prima, onda dvije tačke i nakon toga šta želimo da učinimo sa tim parametrom

a = 1
b = 2
suma = lambda x,y : x + y
c = suma(a,b)
print(c)

#----------------------------------------------------------------------------------------------------------------------
#Višestruki argumenti funkcije (Multiple Function Arguments)
#do sada smo vidjeli da ako funkcija prima parametre, mora se poslati tačno određeni broj vrijednosti tim parametrima
#postoji način da zaobiđemo problem i napišemu funkciju koja će imati varijabilan broj parametara

#ovaj problem zaobilazimo ključnom riječi therest

def funkcija(prvi, drugi, treci, cetvrti, *therest):
    print(prvi)
    print(drugi)
    print(treci)
    print(cetvrti)
    print ("ostali brojevi %s" %(list(therest)))

print (1,2,3,4,5,6,7,8,9)



