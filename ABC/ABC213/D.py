import sys
sys.setrecursionlimit(300000)

N = int(input())

graph = [[] for i in range(N)]

for i in range(N-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

ans = []

for i in range(N):
    graph[i].sort()

def dfs(G, v):
    seen[v] = True
    ans.append(v+1)
    for next_v in G[v]:
        if seen[next_v] == True:
            continue
        dfs(G, next_v)
        ans.append(v+1)

seen = [False for _ in range(N)]
if len(graph[0]) == 0:
    print(1)
else:
    dfs(graph, 0)
    print(*ans)