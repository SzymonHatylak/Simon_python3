# operacje in oraz not in na listach

imiona = ["Ania" , "Amelka" , "Krzysiek" , "Arek" , "Bogdan"]
liczby = [2 , 4 , 6 , 1 , 8 , 9 , 11]

imie = input("podaj jakies imie: ")
liczba = int(input("podaj jakas liczbe: "))

if (imie.capitalize() in imiona):
    print(imie.capitalize() , "To imie jest w liscie")
else:
    print(imie.capitalize() , "Tego imienie nie ma w liscie")

if (liczba not in liczby):
    print(liczba , "Tej liczby nie ma w liscie")
else:
    print(liczba , "Ta liczba jest w liscie")
