from collections import deque

N, M = map(int, input().split())

G = [[] for i in range(N)]
mod = 10 ** 9 + 7

for i in range(M):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

que = deque([0])
dist = [-1 for i in range(N)]
dist[0] = 0
cnt = [0 for i in range(N)]
cnt[0] = 1

while que:
    v = que.popleft()
    d = dist[v]
    for w in G[v]:
        if dist[w] == d + 1:
            cnt[w] = cnt[w] + cnt[v]
        elif dist[w] == -1:
            dist[w] = d+1
            que.append(w)
            cnt[w] = cnt[v]

print(cnt[N-1]%mod)
