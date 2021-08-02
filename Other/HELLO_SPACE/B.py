N, D, H = map(int, input().split())
dh = [map(int, input().split()) for _ in range(N)]
d, h = [list(i) for i in zip(*dh)]

ans = 0.0

def seppen(d, h):
    return((D * h - H * d)/ (D - d))

for i in range(N):
    if ans < seppen(d[i], h[i]):
        ans = seppen(d[i], h[i])

print(ans)
