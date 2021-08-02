nc = list(map(int, input().split()))
N = nc[0]
C = nc[1]
abc = [map(int, input().split()) for _ in range(N)]
a, b, c = [list(i) for i in zip(*abc)]

t = {}
total = 0

for i in range(len(a)):
    for j in range(a[i], b[i]+1):
        if '{}'.format(j) in t:
            t['{}'.format(j)] = t['{}'.format(j)] + c[i]
        else:
            t['{}'.format(j)] = c[i]

for i in t.values():
    if i > C:
        total += C
    else:
        total += i

print(total)
print(t)
