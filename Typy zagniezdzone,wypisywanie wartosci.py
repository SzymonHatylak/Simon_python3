# TYPY ZAGNIEŻDZONE 

imie = "Arkadiusz"
wiek = 29
plec = "mężczyzna"

imie2 = "Wioletta"
wiek2 = 23
plec2 = "kobieta"


osoba1 = ('Arkadiusz', 29, 'mezczyzna')
osoba2 = ('Wioletta', 23, 'kobieta')
osoba3 = ('Kuba', 33, 'mezczyzna')
 
listaGosci = {
                ('Arkadiusz', 28, 'mezczyzna', 602555555),
                ('Wioletta', 22, 'kobieta', 888878362),      #typ zagniezdzony w zbiorze umieszczone sa krotki dzieki temu mozemy wykonywac rozne operacje na zbiorach i krotkach
                ('Kuba', 32, 'mezczyzna', 606235879)  
             }

listaGosci2 = {
                ('Arkadiusz', 28, 'mezczyzna'),
                ('Wiktor', 22, 'kobieta'),
                ('Krzysztof', 32, 'mezczyzna')  
             }

listaGosci3 = listaGosci | listaGosci2

for imie, wiek, plec, telefon in listaGosci:
    print("Imie: ",imie)
    print("Wiek: ",wiek)
    print("Plec: ",plec)
    print("Telefon: ", telefon)
    print("\n")


