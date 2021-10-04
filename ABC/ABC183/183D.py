from collections import defaultdict

N, W = map(int, input().split())

imos = defaultdict(int)

for i in range(N):
    s, t, p = map(int, input().split())
    imos[s] += p
    imos[t] -= p

key = sorted(imos.keys())
use = 0

for i in key:
    use += imos[i]
    if use > W:
        print("No")
        exit()

print("Yes")