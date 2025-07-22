#vakat da krenemo sa funkcijama :D
#jednom kada pređemo funkcije, klase i objekte, mi već tada možemo reći da znamo osnove pythona
#funkcije su koristan način da podijelimo kod u "blokove", to znači da taj blok koda možemo pozvati gdje nam treba poslije
#funkcije je korisno pisati kada imamo neki kod koji bi u suprotnom, da nema funkcija, ponavljali više puta
#funkcija je kao recept

#funkcija se definiše sa ključnom riječi "def", željenim imenom funkcije i ()

def mojaFunkcija():
    print("Pozdrav iz moje funkcije :)")

#funkcije unutar zagrada mogu da primaju argumente
def mojaFunkcija1(korisnickoIme):
    print("Zdravo, %s" %(korisnickoIme))

#funkcije se mogu koristit za računanje i razme natematičke operacije!

def sabiranje(a, b):
    rezultat = a +b
    print(rezultat)


#Kako pozivami finkciju?
#jednostavno, samo napišemo njeno ime i ()
#po potrebi u () stavljamo vrijednosti ako imamo argumente

mojaFunkcija()
mojaFunkcija1("Selma")
sabiranje(5, 35)

#sada možemo preći na klase i objekte
#klasu možemo razumjeti kao šablon, nacrt. Možda čak najslikovitiji način je da ga opišemo kao šablon za kolače
#u tom slučaju bi objekat bio naš kolačić.. i mi od jednog šablona za kolače možemo dobiti gomilu kolačića

#klasa u sebi može da sadrži funkcije, možemo reći da su klase naprednije od funkcija :D

#klase pišemo sa ključnom riječi class

class MojaKlasa:
    varijablica = "Nesto"

    def funkcija(self):
        print("Nesto da se ispisuje")


#self je malo zbunjujuć pojam,  u Python klasama predstavlja konkretni objekat koji je pozvao funkciju ili pristupa varijabli
#chill, bit će valjda više prilike za objašnjenje u nastavku

#vrijednost koju dobijemo iz klase možemo sačuvati unutar neke varijable

varijabla = MojaKlasa()
#vidimo da se klasa poziva na isti način kao i funkcija
#u kodu se možemo snaći pri prepoznavanju klase i funkcije (tokom pozivanja) po tome što IDE većinom promjeni boju klase i funkcije

#preko tačke možemo da pristupimo varijablama u klasi

print(varijabla.varijablica)

#kao što smo rekli, jedna klasa može imati
varijabla1 = MojaKlasa()
#sada vidimo da smo napravili još jednu varijablu/objekt iako smo već napravili jednu ranije
#sada možemo da promjenimo vrijednost varijable za taj objekt

varijabla1.varijablica = "Neko"
print(varijabla.varijablica)
print(varijabla1.varijablica)

#također, možemo da pristupimo i funkciji na isti način na koji smo pristupili i varijabla
varijabla.funkcija()

#postoji jedna jako korisna funkcija u pythonu koja se zove init (__init__())
#ona služi da se objektu odmah daju početne vrijednosti
#također, ova metoda se automatski poziva

#init je nešto kao konstruktor u pythonu
#ova metoda se većinom definira u klasi
#osnovni izgled __init__():

class NekaKlasa:
    def __init__(self, argument1, argument2):
        pass
#hajde da napravimo neku klasu gdje ćemo omogućiti npr. pohranu ljubimaca

class Ljubimci:
    def __init__(self, ime, vrsta):
        self.ime = ime
        self.vrsta = vrsta

#sada kada kreiramo objekat ljubimca, odmah možemo poslati vrijednosti

cicko = Ljubimci("Cicko <3","Macka")



