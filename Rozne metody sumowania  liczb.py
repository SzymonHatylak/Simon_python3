#rozne metody dodawania liczb

liczba = int(input("Podaj sume ilu liczb chcesz dodac: "))
def sumuj_do(liczba):
    suma = 0
    for liczba in range (1, liczba+1):
        suma = suma + liczba
    return suma


def sumuj_do1(liczba):
    suma = (liczba
     for liczba in range(1, liczba+1))
    return sum(suma)

def sumuj_do2(liczba):
    suma = {liczba
     for liczba in range(1, liczba+1)}
    return sum(suma)

def sumuj_do3(liczba):
    suma = [liczba
     for liczba in range(1, liczba+1)]
    return sum(suma)

def sumuj_do4(liczba):
    suma = (1+ liczba) / 2 * liczba
    return(suma)

print("Suma liczb: ", sumuj_do(liczba))
print("Suma liczb: ", sumuj_do1(liczba))
print("Suma liczb: ", sumuj_do2(liczba))
print("Suma liczb: ", sumuj_do3(liczba))
print("Suma liczb: ", sumuj_do4(liczba))
      
    
