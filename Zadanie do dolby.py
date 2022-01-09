
A = [1, 3, 6, 4, 1, 2]
def solution(A):
   m = max(A)
   if m > 0:
       for i in range(1,m):
           if i not in A:
              return i
       else:
          return m + 1
   else:
       return 1
print(solution(A))
