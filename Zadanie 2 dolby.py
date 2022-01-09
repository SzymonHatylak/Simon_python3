numbers = [2, 0, 1, 6]
def solution(numbers):
    minim = numbers [0]
    for x in numbers:
        if x < minim:
            minim = x
    print(minim)
print(solution(numbers))
