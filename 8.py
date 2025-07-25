#regular expressions ili poznatiji kao reqex :)
#ovo je alat koji služi da provjeri uzorke
#npr mi unesemo email i postoji regex da provjeri je li u formatu *@*.*
#ili npr regex može da, ako neko pravi lozinku, obezbjedi da korisnik ne može da sačuva lozinku dok ne doda broj i veliko slovo

#regex je ugrađeni paket pa moramo prvo da kažemo da želimo koristiti ovaj paket u našem kodu
#na primjer kada kliknemo ctrl+f i pretažujemo tekst, to bi se moglo smatrati nekom vrstom regexa
import re

#za regex je potrebno znati metakaraktere
#[] - set karaktera [a - k] znači da bude neko slovo u abecednom rasponu od a do k
#\ - označava da nešto "posebno" slijedi, npr \d daje sve brojeve, a \D daje sve znakove koji nemaju numeričku vrijednost
#. - znači bilo koji karakter  b.ll -> može ball, bill, bell, boll...
#^ - znači da nešto počinje ovim "^zdravo", tražilo bi sve šta počinje sa "zdravo"
#$ - označava da nešto završava ovim "^macka", tražilo bi sve što završava sa "mačka"
#* + ? - znači broj nekih ponavljanja -> * nula ili više, + jedan ili više, ? nula ili jedan
#{} - broj ponavljanja na osnovu unesenog broja -> {3} tri ponavljanja {100} sto ponavljanja
# | -> "jedno ili drugo"
#() - grupa

#od posebnih sekvenci, najbitnija je, pored \d i \D, \s - razmak
#za početak, hajede da uradimo regex za email

mejl = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|org|ba)" 
#na ovaj način smo rekli:
#na početku, mogu se unositi sva mala i velika slova i brojevi, a sa plusem smo rekli da znakova može biti jedan ili više
#@ znači.. jednostavno znak "@", kada nešto isključivo tražimo, možemo to samo napisati u regexu
#nakon "@" ponovo slijede karakeri mala i velika slova ali ovaj put bez brojeva. Sa plusem smo ponovo rekli da tih karaktera mora biti 1 ili više
#treba nam tačka, ali s obzirom da je "." specijalni znak, mi moramo napisati \.
#sa () označavamo grupu, a | znači "ili" -> "od zadane grupe, omogući da korisnik može unijeti com ili edu ili org ili ba"

email = input("Unesite email:")
if(re.search(mejl, email)):
    print("Validan email")
else:
    print("Nije validan email")


#Exception Handling  rukovanje izuzetcima/upravljanje greškama

#recimo da smo napravili neku gršku u kodu i ne možemo da je ispravimo iz nekog razloga
#(nemamo vremena, žuri nam se na ostale funkcionalnosti... ne da nam se)
#znači, koji je god razlog, želimo da nastavimo sa kodiranjem iako imamo error

#ovo možemo rješiti sa try/except blokom koda
#try se koristi kada imamo "opasan kod", pod opasnim kodom smatramo sve što bi moglo srušiti naš kod
#na primjer, unos (input) korisnika se većinom smatra "opasnim kodom" jer korisnici nekada znaju.. biti kreativni
try:
    broj =int(input("Molim vas, unesite željeni broj"))
    print(1/broj)
except ZeroDivisionError:
    print("Nije moguće dijeljenje sa nulom")
except ValueError:
    print("Unijeli ste nešto u string obliku")
finally:
    print("Nest' na kraju")
#na primjer, ovaj kod bi se mogao smatrati opasnim jer korisnik može unijeti 0, a matematički nije moguće broj dijeliti nulom
#ili može se desiti, korisnik onako gladan, da unese "ćevapi" i onda dobijamo 1/ćevapi.. isto nemoguće.. osim ako je to petica, desetka.. tada ima smisla
#radi ovih errora, mi možemo navesti ključnu riječ "try:" znači POKUŠAJ ovo da pokreneš
#ako je to ipak kod koji dovodi do errora, idemo na sljedeći blok koda, a to označavamo ključnom riječi "except"

#ako ne želimo precizirati error, možemo napisati "except Exceptions:"
#na kraju se većinom dodaje "finally:", ovo se na kraju izvršava i većinom se koristi za čišćenje

#---------------------------------------------------------------------------------------------------------------------------
#Setovi (sets)
#setovi su nizovi koji ne dozvoljavaju duplikate da postoje unutar niza
print(set(("ako je to to što mislim da je to.. onda to nije ni malo dobro").split()))

#set je jako koristan u kombinaciji sa još nekim metodama, recimo, hajde da napravimo provjeru ko je prisustvovao svim časovima

predavanje1 = set(["Selma", "Cicko","Hidzreta", "Hanifa"])
predavanje2 = set(["Cicko", "Mujaga"])

#ovo možemo uraditi sa "intersections()"

print(predavanje1.intersection(predavanje2))
#izgleda da je Cicko prisustvovao na oba časa :)

#ili možemo da uradimo provjeru ko je bio samo na jednom času
print(predavanje1.difference(predavanje2))
print(predavanje2.difference(predavanje1))

#ili na primjer, možemo dobiti listu svih polaznika na predavanja

print(predavanje1.union(predavanje2))


#---------------------------------------------------------------------------------------------------------------------
#serijalizacija
#python ima ugrađene biblioteke s kojima se enkodira i dekodira JSON

import json

#kada pričamo o JSONU, on ima 2 formata, ili je string ili u strukturi podataka objekta
#Struktura podataka objekta, u Pythonu, sastoji se od lista i rječnika ugniježđenih jedan u drugi, ovo omogućava korištenje raznih metoda
#String format se uglavnom koristi za prosljeđivanje podataka u drugi program ili učitavanje u strukturu podataka.

# .loads() se koristi da pretvorimo JSON string u Python objekat

json_string = '{"ime": "Selma", "godine": 22}'

print(json.loads(json_string))
nesto = json.loads(json_string)

# suprotno, .dumps() pretvara nazad u JSON

nesto1 = json.dumps(nesto)

