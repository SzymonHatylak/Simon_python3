print("Bedziemy podawac 3 pzrzyste liczby: ")
print()
wynik = 0
i = 0
while i < 3:
    liczba = int(input("Podaj liczbe:"))
    if (liczba % 2 == 0):
        wynik +=liczba
    else:
        print(liczba,"Nie jest liczba parzysta")
        continue
    print("Wynik dodawania liczb to: ",wynik)
    i += 1
