
A =['Andrzej', 'Marek', 'Ania','Bartek', 'Basia', 'Tomek']

def solution(A):
    for x in A:
        newA = [x[::-1]]
        for element in newA:
            if (element[0]!='a'):
                print(newA)
                
solution(A)






        


