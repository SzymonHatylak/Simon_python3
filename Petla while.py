print ("Wypisywanie podanej liczby do 0")
liczba = int(input ("Podaj liczbe z zakresu od 1 do 100: "))
if liczba > 100 or liczba < 0:
    print("Przekroczono wyznaczony zakres mozesz podac tylko liczbe od 1 do 100")
else:
    while liczba >= 0  and liczba <= 100:
        print(liczba)
        liczba -= 1
    
