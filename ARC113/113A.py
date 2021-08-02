import math

K = int(input())

a = math.floor(K ** (1/3))

k = 0

for A in range(1, a+1):
    b = math.floor((K/A) ** 0.5)
    for B in range(A, b+1):
        c = math.floor(K/(A*B))
        for C in range(B, c+1):
            if A == B == C :
                k += 1
            elif A == B or B == C:
                k += 3
            else:
                k += 6

print(k)