import math
a = list(map(int,input().split()))
b = list(map(int,input().split()))
b.append(0)
b.append(a[0]+1)
c = []
b.sort()

if a[1] == 0:
    print(a[0])
else:
    for i in range(a[1]+1):
        if b[i+1]-b[i]-1 > 0:
            c.append(b[i+1]-b[i]-1)

    if not c:
        print(0)
    else:
        d = min(c)
        k = 0

        for i in range(len(c)):
            k += math.ceil(c[i]/d)

        print(k)
