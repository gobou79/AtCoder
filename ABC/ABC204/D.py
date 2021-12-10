import math

N = int(input())
T = list(map(int, input().split()))

half = math.ceil(sum(T) / 2)
total = sum(T)

dp = [[False for i in range(total+1)] for j in range(N+1)]

for i in range(N+1):
    dp[i][0] = True

for i in range(1, N+1):
    for j in range(1, total+1):
        if T[i-1] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = dp[i-1][j-T[i-1]] or dp[i-1][j]

for k in range(half, total+1):
    if dp[N][k]:
        print(k)
        exit()
