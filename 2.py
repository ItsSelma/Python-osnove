#hajde da sada malo detaljnije odradimo operatore

#baš kao i u ostalim programskim jezicima, možemo koristiti razne operacije nad brojevima

broj = 4 + 2 - 1/1.5 * 2.3
print(broj)

#još jedan koristan operator je operator modul (%), on označava ostatak nakon djeljenja
#na primjer ako podijelimo 8/3, dobit ćemo 2 sa ostatkom 2

#hajde da vidimo kako da pišemo eksponente u pythonu
#koristit ćemo ** za eksponente

Zvjezdice = 5 ** 2
print(Zvjezdice)

#kod sabiranja, kada smo radili sa stringovima, vidjeli smo da plus "spaja" stringove

zdravo = "zdravo"
svijete = "svijete"
pozdrav = zdravo + " " + svijete
print(pozdrav)

#čak možemo i pomnožiti string
cao = "cao"
pozdravi = cao * 10
print(pozdravi)

#operatori su dostupni i sa listama

lista1 = [0, 1, 2, 3, 4]
lista2 = [5, 6, 7, 8, 9]

lista3 = lista1 + lista2
print(lista3)

#također, moguće je množiti liste
lista = [1,2,3,4,5,6,7,8,9]
print(lista * 3)

#ili
print([1,2,3] * 4)

#e dobro, hajdemo sada na formatiranje stringa :)

#kod formatiranja stringa, većinom se koristi simbol "%" za formatiranje tj kako bi ubacio vrijednost u string
# %s se koristi za stringove tj. tekst, %d decimalni brojevi, %float

#primjer:

ime = "Selma"

print("Cao! Ja sam %s"%ime)

#možda već sada možemo zamisliti za šta bi se ovo moglo koristiti
# nekada u aplikacijama imamo da upišemo username, mogli bi ovo iskoristiti da npr iskoči prozor koji bi pozdravio korisnika svaki put kada se ulogira

#moguće je koristiti više argumenata

godine = 22

print("Cao, ja sam %s, imam %d godine" %(ime, godine))

# možemo i liste formatirati pomoću %s

listaNeka = [4,5,7,2]

print("ovo je lista %s" % listaNeka)

#----------------------------------------------------------------------------------------
#hajdemo sada da vidimo osnovne string operacije
#najpoznatiji operator za string je operator za dužinu stringa (len())

stringg = "Lorem ipsum cat-dolor sit amet, feline consectetur adipiscing elit."

print (len(stringg))

#uz pomoć ovog operatora vidimo da ovaj string sadrži 67 karaktera

#također, u pythonu, možemo nalaziti lokacije karaktera unutar stringa, to radimo pomoću ".index()"

stringic = "Catnip facilisis, paw-tential maximus, and claw-some adventures await."

print(stringic.index("p"))
#ovdje dobivamo broj 5 jer se u programiranju većinom broj počimajući od nule (0, 1, 2, 3, 4, 5)
#vidimo da jednom kada je pronašao "p", da nije dalje tražio tj. čim nađe prvi karakter koji odgovara traženom, prestaje dalje tražiti

#------------------------------------------------------------------------
#ako želimo da IZBROJIMO karaktere, koristit ćemo "count()"

string1 = "Lorem catsum dolor sit meow, purr sit amet whiskers adipiscing elit. "

print(string1.count("m"))
#ovako smo saznali da ovdje da se karakter "m" pojavljuje 4 puta, a bez potrebe da manuelno brojimo :)

#postoji način da u stringu "odrežemo" dio koji nama odgovara

print(string1[3:10])
#eh, hajde da fino izbrojimo koje je karaktere ovo uzelo kako bi nam bilo jasno ponašanje 
#3-> 0 l 1 o 2 r 3 e - aha! 3. karakter uzima kao
#10 -> 0 l 1 o 2 r 3 e 4 m 5  6 C 7 a 8 t 9 s 10 s
#ah, šta je reći, drugi parametar (10) se ne ponaša kao prvi (3)
#ovo se radi jer ovaj prilaz poslije olaksava matematiku u kodu.. helemnejse

#najlakše je jednostavno prvi parametar početi brojati sa 0 (0, 1, 2, 3..), a drugi parametar sa 1 (1, 2, 3, 4) 