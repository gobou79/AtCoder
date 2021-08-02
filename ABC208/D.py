inf = float("inf")

N, M = map(int, input().split())

d = [[inf for i in range(N)] for i in range(N)]

for i in range(N):
    d[i][i] = 0

for i in range(M):
    a, b, c = map(int, input().split())
    d[a-1][b-1] = c

ans = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            d[i][j]= min(d[i][j],d[i][k]+d[k][j])
            if d[i][j] != inf:
                ans += d[i][j]

print(ans)