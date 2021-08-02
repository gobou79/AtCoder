N = int(input())
a = list(map(int, input().split()))

m = min(a) * len(a)

ind = [a.index(min(a))]

k = 1

b = []
c = []
if ind[0] != 0:
    b.appned(a[:ind[0]-1])
for i in range(0, k-1):
    b.append(a[ind[i]+1:ind[i+1]-1])
if ind[k] != len(a)-1:
    b.append(a[ind[k]+1:])
for i in range(len(b)):
    c.append(min(b[i] * len(b[i])))
if max(c) > m:
    m = max(c)
else:
    break

print()