#sposob tradycyjny

potegidwojki = []
for element in range(1,21):         #21 poniewaz w range oststni element nie jest brany pod uwage
    potegidwojki.append(element**2)
print(potegidwojki)

liczbyparzyste = []
for element in range(1,21):
    if(element % 2 == 0):
        liczbyparzyste.append(element)
print(liczbyparzyste)


#Dla tych samych zadan wykorzystanie formul listownych

potega2 = [element**2
           for element in range(1,21)]
print(potega2)

parzyste2 = [element for element in range(1,21)
             if(element % 2 == 0)]
print("Parzyste metoda listowna", parzyste2)


dodawanie = [element
             for element in range(101)]
print (sum(dodawanie))
                                                   
