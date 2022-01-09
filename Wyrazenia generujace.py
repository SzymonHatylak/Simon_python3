#Wyrazenia generujace
import sys
wyrazenie = [element for element in range(400)
             if element % 2 == 0]

print(wyrazenie)


generator = (element for element in range(400)
             if element % 2 == 0)
print(generator)

for item in generator:
    print(item)

#print(sys.getsizeof(wyrazenie))
