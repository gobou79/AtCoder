import math

N = int(input())


X = list(map(int, input().split()))
x = []

for i in X:
    for j in range(2, 51):
        if i % j == 0:
            x.append(j)
            break
l = set(x)
L = list(l)

for i in L:
    k = 0
    for j in X:
        if j % i == 0:
            k += 1
        else:
            break
    if k == N:
        print(i)
        break
    
if k != N:
    y=1
    for a in L:
        y=a*y//math.gcd(a,y)
    print(y)