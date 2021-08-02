import math

N = int(input())

k = 0
a = 2
s = set()


while a > 0:
    b = math.floor(math.log(N, a))
    if b < 2:
        break
    else:
        for i in range(2, b+1):
            s.add(a ** b)
    a += 1


print(N - len(s))
