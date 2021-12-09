N, W = map(int, input().split())
weight = []
value = []
for i in range(N):
    w, v = map(int, input().split())
    weight.append(w)
    value.append(v)

value_max = sum(value)

dp = [[float('inf') for i in range(value_max+1)] for j in range(N+1)]

dp[0][0] = 0

for i in range(N):
    for j in range(value_max+1):
        if value[i] > j:
            dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = min(dp[i][j-value[i]]+weight[i], dp[i][j])

ans = 0
for i in range(value_max+1):
    if dp[N][i] <= W:
        ans = i

print(ans)