print("Operatory logiczne")
print("Porownamy 2 liczby z pewnego zakresu")
print("\n")

a = int(input("Podaj pierwszą liczbe: "))
b = int(input("Podaj druga liczbe: "))

if a > 0  and b < 100 and b > 0:
    print("Liczby sa z przedzialu od 0 do 100")
elif a < 0 and b > 0:
    print("Pierwsza liczba jest <0,druga liczba jest >0")
else:
    print("Druga liczba jest <0,pierwsza liczba jest >0")
if a == 0 and b == 0:
    print("Obie liczby sa zerami")
elif a < 0 and b < 0:
    print ("Obie liczby sa <0")
elif a<0 or b < 0:
    print("Jedna z podanych liczb jest <0")
if a == b:
    print("Podane liczby sa rowne")
    
