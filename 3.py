#kod stringNeki[], ako stavimo jedan broj, onda ćemo dobiti samo karakter sa tim indeksom (mjestom u stringu)
#ako izostavimo prvi parametar, a drugi napišemo npr. string[ :5], ovdje će isjeći string i uzeti OD POČETKA, pa do karaktera sa indeksom 5
#ako izostavimo drugi parametar, a prvi napišemo npr. string[5: ], ovdje će isjeći string i uzeti OD KRAJA. pa do karaktera sa nideksom 5

#kao parametar se mogu staviti i negativni brojevi, na taj način možemo krenuti brojanje indeksa od kraja

#možemo i preskakati karaktere sa 3. parametrom!
#primjer:

recenica = "Nije vruce, nego nekakva sparina.."
print(recenica[7:15:2])

#znači, možemo reći da je sintaksa [početa:kraj:korak]

#hajde da sada razmislimo kako da okrenemo riječ/rečenicu
#znamo da ne navesti početak znači počni od prvog elementa, a ne navesti kraj znači idi skroz do kraja
#isto tako znamo da se negativni brojevi koriste za kretanje od kraja
#na osnovu ovog znanja možemo napisati sljedeće:

print(recenica[::-1])
#dobili smo željeni rezultat :D

#uz sve navedeno, dostupno nam je i pretvaranj u velika slova i obratno, sve u mala slova

print(recenica.upper())
print(recenica.lower())

#imamo i metode koje vraćaju boolean vrijednost
print(recenica.startswith("Nije"))
print(recenica.endswith("nekineartikulisanikarakteri"))

#imamo i metodu koja može da od jedne rečenice da napravi listu, na osnovu zadatog karaktera, najčešće razmaka

PozdravSvijetu = "Zdravo svijete"
nekiNiz = PozdravSvijetu.split(" ") 

#vizuelno, ovdje se dešava: "Zdravo svijete!" 
 #                            ↓ split(" ")
#                         ['Zdravo', 'svijete!']


#hajde sada da vidimo kako uvjeti rade u pythonu

#python koristi boolean logiku, tj provjerava se je li nešto tačno ili nije tačno i na osnovu toga se ispunjava ili ne ispunjava uvjet

broj = 1
print(broj == 1)
print(broj == 3)
print(broj < 5)
#ako == znači jednako, onda != znači da nije jednako

ime = "Selma"
godine = "22"

if(ime == "Selma" and godine == "22"):
    print("ćao, ja sam Selma i imam 22 godine")

#ovdje vidimo jedan operator koji nismo prije viđali, a to je operator "and"
#on je boolean operator i vraća tačno samo ako su oba slučaja tačna

#može se koristiti "or" ako želimo da bude tačno u slučaju da je jedan ili više parametara tačno, netačno je samo ako ništa nije tačno

#pored ovih operatora, postoji i "in" operator
#ovaj "in" operator provjerava da li se nešto nalazi u nizu

voce = "ananas"

if voce in ["ananas", "banana", "orasi", "mango"]:
    print("Da, u nizu se nalazi zadano voce")



#u pythonu imamo nešto što se zove "pass", on ne radi ništa :)
#zašto bi nam trebalo nešto što ne radi ništa??
#to je korisno ako negdje moramo da napišemo kod, a nismo još to uradili
#da ne bi prijavljivalo grešku, možemo staviti pass

izraz = False
drugi_izraz = True
if izraz is True:

    pass
elif drugi_izraz is True: # else if
    
    pass
else:
    pass

#sljedeći operator je "is" operator
#na prvu nam se može učiniti da je on isti kao "==" operator, ali to nije tačno
#ako imamo neko varijablu sa istom vrijednosti, npr 4, "==" će vratiti true jer imaju JEDNAKU vrijednost
#ponovo, ako imamo neko varijablu sa istom vrijednosti, npr 4, "is" neće vratiti true jer, iako imaju istu vrijednost, to NISU iste varijable

x = [1,2,3]
y = [1,2,3]
print(x == y) 
print(x is y)

# "not" operator
# not operator "okreće" vrijednosti, isto kao što smo imali u npr c++ !nekaVrijednost, i onda ako je bilo true dobit ćemo false i obrnuto
#"not" operator radi istu stvar

print(not False) 
print((not False) == (False))

