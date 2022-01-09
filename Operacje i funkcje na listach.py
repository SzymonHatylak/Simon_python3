# Operacje i funkcje na listach

imiona = ["Ania" , "Amelka" , "Szymon"]
liczby = [1 , 2 , 44 , 8 , 6 , 1 , 9 , 1]

#sprawdzenie dlugosci listy imiona
#print (len(imiona))

'''
#Dodawanie do isty kolejnej wartosci wartosc dodaje sie na koncu listy
imiona.append("Tomek")
print(imiona)
'''

'''
#Rozszerzenie listy o element
imiona.extend(["Tomek"])
print (imiona)
'''

'''
#wstawienie do indeksu 0 liczby 123
liczby.insert (0,123)
print (liczby)
'''

'''
#wskazanie indeksu pod ktorym znajduje sie dany element
print(liczby.index(44))
'''

'''
# sortowanie liczb od najmniejszej do najwiekszej
liczby.sort()
print(liczby)

#sortowanie od najwiekszej do najmniejszej
liczby.sort(reverse = True)
print(liczby)
'''

'''
# sprawdzanie ile razy w liscie wystepuje dany element
print(liczby.count(1))
'''

'''
#ta funkcja usuwa z listy oststni element
liczby.pop()
print(liczby)
'''

'''
#funkcja usunie pierwsze wystapienie danego elementu w liscicie
liczby.remove(1)
print(liczby)
'''

'''
#Ta funkcja czysci cala zawartosc listy
liczby.clear()
print(liczby)
'''

'''
# Ta funkcja odwraca kolejnosc w liscie od ostatniego do pierwszego
liczby.reverse()
print(liczby)
'''

'''
#wypisanie najmniejszej oraz najwiekszej wartosci z listy
print(min(liczby))
print(max(liczby))
'''






