print("Bedziemy dodawac liczby wykorzystujac petle for:")
print()
wynik = 0
y = int(input("Ile liczb chcesz dodac: "))
for i in range(y):
    if y >= 2:
        x = int(input("Podaj liczby: "))
        wynik += x
    else:
        print("Musisz podac co najmniej 2 liczby")
        break 
    print()
    print ("Wynik dodawania to: ",wynik)
