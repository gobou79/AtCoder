from collections import defaultdict

N = int(input())

imos = defaultdict(int)

for i in range(N):
    a, b = map(int, input().split())
    imos[a] += 1
    imos[a+b] -= 1

key = sorted(imos.keys())
ans = [0 for i in range(N+1)]
before = 0
cnt = 0

for i in key:
    ans[cnt] += i - before
    cnt += imos[i]
    before = i

print(*ans[1:])