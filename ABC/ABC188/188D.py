from collections import defaultdict

N, C = map(int, input().split())

imos = defaultdict(int)

for i in range(N):
    a, b, c = map(int, input().split())
    imos[a] += c
    imos[b+1] -= c

key = sorted(imos.keys())
ans = 0
before = 0
money = 0

for i in key:
    if money > C:
        ans += C * (i-before)
    else:
        ans += money * (i-before)
    before = i
    money += imos[i]

print(ans)
