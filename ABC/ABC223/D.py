from collections import defaultdict
import heapq

N, M = map(int, input().split())

A, B = [], []
g = [[] for i in range(N)]
d = defaultdict(int)

for i in range(M):
    a, b = map(int, input().split())
    d[b-1] += 1
    g[a-1].append(b-1)

h = []

for i in range(N):
    if d[i] == 0:
        h.append(i)

heapq.heapify(h)

ans = []

while len(h) > 0:
    n = heapq.heappop(h)
    ans.append(n+1)
    for i in g[n]:
        d[i] -= 1
        if d[i] == 0:
            heapq.heappush(h, i)

if len(ans) == N:
    print(*ans)
else:
    print(-1)