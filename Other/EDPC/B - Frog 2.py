N, K = map(int, input().split())
h = list(map(int, input().split()))

dp = [0 for i in range(N+1)]

for i in range(2, N+1):
    k = min(i, K+1)
    a = float('inf')
    for j in range(1, k):
        a = min(a, dp[i-j] + abs(h[i-j-1] - h[i-1]))
    dp[i] = a

print(dp[N])