#hajde da sada izvježbamo ono što programiranje ne bi bilo programiranje bez ovoga
#a to su petlje
#prvo idemo na for petlju
#for petlja se koristi za iterativno ponavljanje, npr. stavili smo da se ponavlja nešto onoliko puta koliko je elemenata.. ili baš neki određen broj puta.. npr 10

brojevi = [1, 2, 3, 4, 5]

for i in brojevi:
    print(i)

# Kažemo: "Za svaki broj u listi 'brojevi', uzmi ga privremeno i nazovi ga 'i' ".
# Taj 'i' je kao kutija koja svaki put dobije novi broj iz liste.
# Prvi prolaz: i = 1 → print(i) → ispiše se 1
# Drugi prolaz: i = 2 → ispiše 2
# I tako redom... sve dok ne dođe do kraja liste.

#navela sam da for petlja se može vrtiti i određen broj puta koji smo naveli.. kako to da uradimo
#to radimo sa metodom "range()"

for x in range(7):
    print(x)

#naravno, ispisat će se 7 elemenata počevši od 0 (0,1,2,3,4,5,6)

#prije je postojala i metoda xrange, ali se ona danas skoro i ne koristi.. Ona se je koristila u python 2 verziji
#ali sada se svakako koristi većinom python 3 verzija pa ova metoda nije ni bitna

#while loop

#while petlja se vrti sve dok je boolean izraz ispunjen
#pod ispunjen misli se na tačan izraz

brojac = 0
while brojac < 6:
   print(brojac)
   brojac += 1

#ovdje se kod ovako ponaša:
#brojač je postavljen na 0, nakon toga idemo u while petlju
#postavlja se pitanje: da li je 0 manje od 6? Naravno da jeste, ulazimo u sadržaj petlje
#preko printa se ispisuje 0, a brojač se povećava na 1
#ponovo se ponavlja while petlja, samo sada sa brojačem vrijednosti 1
# da li je 1 manje od 6? Naravno da jeste, ulazi se ponovo u sadržaj petlje i izvršavaju se iste linije: printanje i povećavanje brojača
#to se ponavlja sve dok brojač ne dođe do broja 6
#da li je 6 manje od 6? Naravno da nije i onda se ova petlja prekida i mi izlazimo iz petlje
#na ovaj način smo dobili brojeve od 0 do 5

#u pythonu postoje i naredbe break i continue
#break je naredba koja prekida petlju
#continue je naredba koja preskače sljedeći blok koda
brojac = 0
while True:
    print(brojac)
    brojac += 1
    if brojac >= 5:
        break

#ovo znači: "u slučaju da brojač bude jednak ili veći od 5, prekini petlju"
#ovdje bi imali beskonačnu petlju da nema ove break naredbe jer je while dobio  tačno kao parametar

for x in range(10):
    if x % 2 == 0:
        continue
    print(x)

#ovdje ćemo dobiti samo neparne brojeve
# zašto je to tako?
#u ovoj for petlji, imamo uslov "da li je x djeljiv sa 2?" znamo da jedini brojevi koji su djeljivi sa 2 su parni brojevi
#znači, u slučaju da je parni broj, preskoči sljedeći broj koda
#znači do bloka koda koji je namjenjen za printanje vrijednosti, doći će samo x koji nema paran broj za vrijednost

#u pythonu postoji i "else", samo treba imati na umu da se to izvršava i kada imamo continue uslov

brojac=0
while(brojac<5):
    print(brojac)
    brojac +=1
else:
    print("Brojac je dosegao vrijednost %d" %(brojac))

for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("Ovo se ne ispisuje jer je for petlja prekinuta zbog break, a ne zbog neuspjeha u uvjetu.")

#ovdje imamo jednu while petlju koja broji od 0 do 4 – dok je brojac manji od 5, petlja se vrti
#svaki put ispiše trenutni brojac i onda ga poveća za 1
#kad brojac više nije manji od 5, izvrši se dio ispod "else", tj. kada se petlja završi prirodno
#ispisuje se poruka da je brojac dostigao 5

#u drugom dijelu koristimo for petlju koja ide od 1 do 9
#ako je broj djeljiv sa 5 (i%5==0), petlja se odmah prekida naredbom break
#inače se broj ispisuje – to su 1,2,3,4 jer 5 prekida petlju
#zato se dio "else" ne izvršava, jer je petlja nasilno prekinuta sa break
#da nije bilo break-a, "else" bi se uredno izvršio kad završi normalno
#ovo je zgodno ako hoćeš znati jel' petlja išla do kraja ili ju je nešto prekinulo


