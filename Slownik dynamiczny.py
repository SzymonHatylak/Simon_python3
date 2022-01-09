#Zadanie slownik dynamiczny

slownik = {}

print("Witaj uzytkowniku to jest slownik dynamiczny:")
print()

print("Ponizej menu uzytkownika")
print()
while(True):
    print("1 Dodaj definicje")
    print("2 Spradz definicje")
    print("3 Usuwanie definicji")
    print("4 Zakonczenie programu")
    print()

    wybor = input("Co chcesz zrobic?: ")
    print()

    if(wybor == "1"):
        slowo = input ("Podaj slowo klucz: ")
        definicja = input ("Podaj definicje slowa kluczowego: ")
        slownik[slowo] = definicja
        print("Dodano definicje do slownika ")
        print()
    elif wybor == "2":
        slowo = input ("Jakiej definicji szukasz?: ")
        print()
        if slowo in slownik:
            print(slownik[slowo])
            print()
        else:
            print("Ta definicja nie wystepuje w slowniku")
            print()
    elif wybor == "3":
        slowo = input ("Jakie slowo chcesz usunac: ")
        print()
        if slowo in slownik:
            del slownik[slowo]
            print("Usunieto definicje o nazwie", slowo)
            print()
        else:
            print(slowo, "Ta definicja nie wystepuje w slowniku")
            print()
    elif (wybor == "4"):
        print("Koniec programu ")
        break
    else:
        print("Nie mam takiej wartosci w menu: ")
        print()
        
    
    

