"""
    wyrażenie słownikowe
"""

names = {"Arkadiusz", "Wioletta", "Karol", "Bartłomiej", "Jakub", "Ania", "Amelia"}

numbers = [1, 2, 3, 4, 5, 6]

celcius = {'t1': -20, 't2': -15, 't3': 0, 't4': 12, 't5': 24}



nameLenght = {name:len(name)
              for name in names
              if name.startswith ("A")}

print(nameLenght)


sumaliczb = {number : number ** 2
             for number in numbers
             if number % 2 ==0}

print(sumaliczb)

fahrenhite = {
               key : celcius * 1.8 + 32
               for key, celcius in celcius.items()
    }

print("Temp w fahrenhite: ", fahrenhite)
