# Program do liczenie powierzchni figur
import math
from enum import IntEnum

Menu_Figury = IntEnum('Menu_Figury', 'Kwadrat Prostokat Trojkat Trapez Kolo ZakonczenieProgramu')

print("Ponizej menu, w ktorym mozesz wybrac figure ktorej pole chcesz policzyc")
while(True):
    print("1 Kwadrat: ")
    print("2 Prostokat")
    print("3 Trojkat")
    print("4 Trapez")
    print("5 Kolo")
    print("6 Zakonczenie programu")
    print()


    wybor = int(input("Co chcesz policzyc: "))

    def pole_kwadratu(a):
        return a*a

    def pole_prostokata(c, d):
        return c*d

    def pole_trojkata (a, h):
        return 0.5 * a * h

    def pole_trapezu(a, b, h):
        return(a+b)/2 * h

    def pole_kola(r):
        return math.pi*r**2

    if wybor == Menu_Figury.Kwadrat:
        a = int(input("Podaj bok kwadratu a = "))
        print("pole kwadratu = ", pole_kwadratu(a))
        print()
        

    if wybor == Menu_Figury.Prostokat:
        c = int(input("Podaj 1 bok prostokata a = "))
        d = int(input("Podaj 2 bok prostokata b = "))
        print("Pole Prostokata = ", pole_prostokata(c, d))
        print()

    if wybor == Menu_Figury.Trojkat:
        a = int(input("Podaj bok trojkata a = "))
        h = int(input("Podaj wysokosc trojkata h = "))
        print("Pole Prostokata = ", pole_trojkata(a, h))
        print()

    if wybor == Menu_Figury.Trapez:
        a = int(input("Podaj bok trapezu a = "))
        b = int(input("Podaj 2 bok trapezu b = "))
        h = int(input("Podaj wysokosc trapezu h = "))
        print("Pole Prostokata = ", pole_trojkata(a, h))
        print()
    if wybor == Menu_Figury.Kolo:
        r = int(input("Podaj promienkola r = "))
        print("pole kwadratu = ", pole_kola(r))
        print()

    if wybor == Menu_Figury.ZakonczenieProgramu:
        print("Koniec programu: ")
        break
    
