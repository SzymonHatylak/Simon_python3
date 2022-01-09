print("Zabawa w szukanie liczby masz 5 prob")
szukana_liczba = 40

i = 0 
while i < 5:
    podana_liczba = int(input("Podaj dodatnia liczbe od 1 do 100: "))
    if (szukana_liczba == podana_liczba):
        print("Zgadles :)")
        break
    elif (szukana_liczba > podana_liczba):
        print("Podales za mala liczbe,podaj jeszcze raz ")
    elif (szukana_liczba < podana_liczba):
        print("Podales za duza liczbe, podaj jeszcze raz")
    i += 1

