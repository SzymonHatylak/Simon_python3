#slownik 2
slownik = {}
print("Witaj uzytkowniku to jest slownik dynamiczny wersja 2")
print()

print("Poniżej menu w ktorym mozesz wybrac co chcesz zrobic:")
print()

while(True):
    print("1: Dodaj rekord do slownika")
    print("2: Sprawdz rekord")
    print("3: Usun rekord")
    print("4: Konczenie pracy programu")
    print()

    wybor = input("Co chcialbys zrobic?: ")
    print()

    if wybor == "1":
        rekord = input("Podaj slowo klucz: ")
        definicja = input("Podaj definicje slowa kluczowego: ")
        print()
        slownik[rekord] = definicja
        print("Definicja dodana do slownika ")
        print()
    elif wybor == "2":
        rekord = input("Jakie slowo chcesz sprawdzic?: ")
        print()
        if rekord in slownik:
            print (slownik[rekord])
            print()
        else:
            print(rekord, "Definicji tego slowa nie mam w slowniku: ")
            print()
    elif wybor == "3":
        rekord = input("Podaj slowo ktore chcesz usunac: ")
        if rekord in slownik:
            del slownik[rekord]
            print("Definicja zostala usunieta")
            print()
        else:
            print(rekord, "To slowo nie wystepuje w slowniku: ")
            print()
    elif wybor == "4":
        print("Zakonczyles prace programu, uruchom program ponownie")
        break
    else:
        print("Twoj wybor nie wystepuje w menu uzytkownika ")
        print()

