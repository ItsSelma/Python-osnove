#znaci .loads() : json -> python dictionary
# i .dumps() : python dictionary -> json

#ZNAČI json se koristi da bi mogli poslati informacije u 
# tekstualnom formatu, a Python dictionary nam treba kako
#  bi mogli fino sami da manipulisemo podacima tim u kodu. 
# Iz json u python dictionari se pretvara funkcijom 
# loads(), a obrnuto funkcijom .dumps()

#pickle je ugrađeni Python modul koji omogućava serializaciju i deserializaciju Python objekata.
#Serializacija: pretvaranje Python objekta (npr. rječnika, liste, klase) u binarni format koji 
# se može sačuvati u fajl ili poslati preko mreže.
#Deserializacija: vraćanje tog binarnog formata nazad u originalni Python 

#pickle ima samo u pythonu 
import pickle

korisnik = {"ime": "Selma", "godine": "22", "student": "true" }

pikle_string = pickle.dumps(korisnik)

print(pickle.loads(pikle_string))

#------------------------------------------------------------------------------------
#partial functions
#koristimo  functool biblioteku
#parcijalne funkcije se koriste kako bi uzeli funkciju koja ima neki broj parametara i od nje napravimo novu funkciju
#ta nova funkcija isto ima parametra, ali neki parametri su pretvoreni u kostante pa nema potrebe za daljim slanjem tih nekih parametara

#na primjer, evo jedne funkcije koja vraća da li je prvi broj veći od drugog

def vece(a, b):
    return a >b

print(vece(20, 30))
print(vece(30, 20))

#eh, kako bi napravili funkciju koja može da primi npr broj 40 i koja automatski gleda je li npr. b = 30, veće ili manje od b

#"manuelni" način bi bio sljedeći

def vece1(n):
    return lambda a: a > n

veceod30 = vece1(30)

print(veceod30(40))
print(veceod30(20))

#vidimo da bobivamo zeljeni rezultat
#hajde da uradimo istu stvar sa pickle

from functools import partial

def veceOd(a, b):
    return a > b

veceOd40 = partial(veceOd, b=40)

print(veceOd40(50))
print(veceOd40(30))
#i ovdje vidimo kako je b pretvoren u kostantu i ne moramo vise unositi b

#--------------------------------------------------------------------------------------------------------------
#code introspekcija
#Introspekcija koda je sposobnost ispitivanja klasa, 
# funkcija i ključnih riječi kako bi se znalo šta su, šta rade i šta "znaju"

#python ima ugrađene funkcije koje pomažu nama u ovom procesu

# help()
# dir() 
# hasattr() 
# id() 
# type() 
# repr() 
# callable() 
# issubclass() 
# isinstance() 
# __doc__ 
# __name__

#najvažnija je help funkcija

#---------------------------------------------------------------------------------------------------------------------
#closures - zatvaranja

#već smo vidjeli jedan primjer gdje smo imali closures (lambda iznad)

#closures su često funkcije u funkciji

def dodaj_brojeve():
    brojevi = []

    def dodajBrojeve_unutrasnja(x):
        brojevi.append(x)
        print(brojevi)
    
    return dodajBrojeve_unutrasnja

dodaj_broj = dodaj_brojeve()
dodaj_broj(3)
dodaj_broj(4)
dodaj_broj(5)

#dobra stvar u ovom načinu je to što se ovdje varijabla "brojevi" nalazi unutar funkcije

