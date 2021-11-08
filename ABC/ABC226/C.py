import sys
sys.setrecursionlimit(10 ** 9)

N = int(input())

def dfs(G, v):
    visited[v] = True
    for next_v in G[v]:
        if visited[next_v-1] == True:
            continue
        dfs(G, next_v-1)

G = []
T, K = [], []
visited = [False for i in range(N)]
visited[-1] = True

for i in range(N):
    a = list(map(int, input().split()))
    G.append(a[2:])
    T.append(a[0])
    K.append(a[1])

ans = 0

for i in G[-1]:
    if visited[i-1]:
        continue
    else:
        dfs(G, i-1)

for i in range(N):
    if visited[i]:
        ans += T[i]

print(ans)