N, W = map(int, input().split())
w, v = [], []
for i in range(N):
    a, b = map(int, input().split())
    w.append(a)
    v.append(b)

dp = [[0 for i in range(W+1)] for j in range(N+1)]

for i in range(N):
    for j in range(W+1):
        if w[i] > j:
            dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = max(dp[i][j-w[i]]+v[i], dp[i][j])

print(dp[-1][-1])