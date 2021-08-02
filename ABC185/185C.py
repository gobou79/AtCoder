import math


l = int(input())
a = l-1

def fact(h):
    k = 1
    for i in range(1, h+1):
        k = k * i
    return k


n = math.comb(a,11)
N = fact(a)//fact(a-11)//fact(11)

print(n)
print(N)