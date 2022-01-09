print("Bedziemy wypisywac liczby podzielne przez 5 i niepodzielne przez 7")
print()
zakres = int(input("Podaj zakres z jakiego chcesz obliczyc liczby: "))

for i in range(zakres):
    if(i % 5 == 0 and i % 7 == 1):
        print("Te liczby to: ",i)
