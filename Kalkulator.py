print("To jest prosty kalkulator,nalezy dokonac wyboru dzialania, instrukcja ponizej:")
print("\n")
print("Kalkulator posiada nastepujaca liste dzialan:")
print("Jezeli wybierzesz 1 wykona +")
print("Jezeli wybierzesz 2 wykona -")
print("Jezeli wybierzesz 3 wykona *")
print("Jezeli wybierzesz 4 wykona /")
print("Jezeli wybierzesz 5 wykona **")
print("Jezeli wybierzesz 6 wykona %")
print("\n")
print("Dokonaj wyboru:")
wybor = int(input("Podaj liczbe od 1-6 wg. instrukcji powyzej:"))
a = int(input("Podaj pierwsza liczbe:"))
b = int(input("Podaj druga liczbe:"))
if wybor == 1:
    print("Wybrales dodawanie, wynik to:",a+b)
elif wybor == 2:
    print("Wybrales odejmowanie, wynik to:",a-b)
elif wybor == 3:
    print("Wybrales mnozenie, wynik to:",a*b)
elif wybor == 4:
   
    if b == 0:
       print("To dzialanie nie moze byc wykonane nie mozna dzielić przez zero")
    else:
       print("Wybrales dzielenie, wynik to:",a/b)
elif wybor == 5:
    print("Wybrales potegowanie, wynik to:",a**b)
elif wybor == 6:
    print("Wybrales dzielenie modulo, wynik to:",a%b)
                  
      
