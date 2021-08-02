N = int(input())

n = str(N)
l = len(n)
m = l // 2

A = list(n)

if l % 2 == 1:
    k = 10 ** ((l-1)//2) - 1
    if k <= 0:
        print(0)
    else:
        print(k)
else:
    a = A[:m]
    b = A[m:]
    c = int(''.join(a))
    d = int(''.join(b))
    if c > d:
        print(c-1)
    else:
        print(c)
