from collections import deque

N, M = map(int, input().split())
G = [[] for i in range(N)]

mod = 10 ** 9 + 7

for i in range(M):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

dist = [-1] * N
dist[0] = 0
que = deque([0])

d_min = 10 ** 10
ans = 0

cnt = [1] * N

while que:
    v = que.popleft()
    d = dist[v]
    for w in G[v]:
        if dist[w] == d + 1:
            cnt[w] += 1
        elif dist[w] == -1:
            if w == N-1:
                can = d + 1
                if can <= d_min:
                    d_min = can
                    ans += cnt[v]
            else:
                dist[w] = d + 1
                cnt[w] = cnt[v]
                que.append(w)

print(ans%mod)