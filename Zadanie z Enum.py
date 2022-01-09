# zadanie z enum
from enum import IntEnum
print("Przypisywanie kolorów do dni tygodnia : ")
print()
print("Ponizej menu:")
print()

Menu = IntEnum ("Menu", 'Poniedzialek, Wtorek, Sroda, Czwartek, Piatek, Sobota, Niedziela')

print("1 Poniedzialek")
print("2 Wtorek")
print("3 Sroda")
print("4 Czwartek")
print("5 Piatek")
print("6 Sobota")
print("7 Niedziela")
print()

wybor = int(input("Wybierz dzien tygodnia: "))
print()

if wybor == Menu.Poniedzialek:
    print("Czarny")

if wybor == Menu.Wtorek:
    print("Niebieski")

if wybor == Menu.Sroda:
    print("Pomaranczowy")

if wybor == Menu.Sroda:
    print("Zolty")

if wybor == Menu.Czwartek:
    print("Rozowy")

if wybor == Menu.Piatek:
    print("Czerwony")

if wybor == Menu.Sobota:
    print("Zielony")

if wybor == Menu.Niedziela:
    print("Szary")
