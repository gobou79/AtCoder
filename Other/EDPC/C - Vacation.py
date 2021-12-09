N = int(input())
A = []
for i in range(N):
    a = list(map(int, input().split()))
    A.append(a)

dp = [[0 for i in range(N)] for _ in range(3)]
dp[0][0] = A[0][0]
dp[1][0] = A[0][1]
dp[2][0] = A[0][2]

for i in range(1, N):
    for j in range(3):
        pos = [0, 1, 2]
        pos.remove(j)
        dp[j][i] = max(dp[pos[0]][i-1], dp[pos[1]][i-1]) + A[i][j]

print(max(dp[0][-1], dp[1][-1], dp[2][-1]))