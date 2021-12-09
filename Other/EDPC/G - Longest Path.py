import sys

sys.setrecursionlimit(10 ** 6)

N, M = map(int, input().split())
graph = [[] for i in range(N)]

for i in range(M):
    x, y = map(int, input().split())
    graph[x-1].append(y-1)

dp = [-1 for i in range(N)]

def rec(v):
    if dp[v] != -1:
        return dp[v]
    ans = 0
    for u in graph[v]:
        ans = max(ans, rec(u)+1)
    dp[v] = ans
    return dp[v]

ans = 0
for i in range(N):
    ans = max(ans, rec(i))

print(ans)