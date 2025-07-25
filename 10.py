#Dekoratori (decorators)
#dekoratori omogućavaju rad sa malim promjenama nad pozovljivim objektima kao funkcije, metode i klase
#dekorator je funkcija koja "proširuje" drugu funkciju, ne dirajući  baznu funkciju

def dodaj_luka(funkcija):
    def wrapper():
       print("Ako neces pricati s nekim, dodaj luka")
       funkcija()
    return wrapper

@dodaj_luka
def naruci_cevape():
    print("Evo ga vasa desetka 🍽")

naruci_cevape()