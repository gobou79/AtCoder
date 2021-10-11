N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp = [[0 for i in range(3001)] for j in range(N)]
mod = 998244353

for i in range(N):
    cnt = 0
    for j in range(3001):
        if i == 0:
            if a[i] <= j and j <= b[i]:
                cnt += 1
                dp[i][j] = cnt % mod
            elif j > b[i]:
                dp[i][j] = cnt % mod
        else:
            cnt = 0
            if j <= a[i]:
                dp[i][j] = dp[i-1][j] % mod
            elif a[i] < j and j <= b[i]:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % mod
            else:
                dp[i][j] = dp[i][j-1] % mod

print(dp[-1][-1] % mod)