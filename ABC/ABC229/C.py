from collections import defaultdict

N, W = map(int, input().split())

d = defaultdict(int)

for i in range(N):
    a, b = map(int, input().split())
    d[a] += b

ds = sorted(d.items(), reverse=True)

ans = 0
w = 0

for i in range(len(ds)):
    m = ds[i][1]
    if w + m <= W:
        w += m
        ans += m * ds[i][0]
    else:
        ans += (W-w) * ds[i][0]
        break

print(ans)