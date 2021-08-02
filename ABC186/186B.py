import itertools

a = list(map(int, input().split()))
b = [list(map(int, input().split())) for l in range(a[0])]

c = list(itertools.chain.from_iterable(b))

m = min(c)

k = 0

for i in c:
    k += i-m

print(k)