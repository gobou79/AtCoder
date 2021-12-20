from collections import deque

H, W = map(int, input().split())
adj = [[] for i in range(H*W)]
A = []
for i in range(H):
    w = list(input())
    A.append(w)

dist = [[-1 for i in range(W)] for j in range(H)]

dist[0][0] = 1
dhdw = [(0, 1), (1, 0)]

q = deque([(0, 0)])

while q:
    h, w = q.popleft()
    for dh, dw in dhdw:
        nh, nw = h + dh, w + dw
        if 0 <= nh < H and 0 <= nw < W and A[nh][nw] == '.' and dist[nh][nw] < dist[h][w]:
            if dist[nh][nw] == -1:
                q.append((nh, nw))
            dist[nh][nw] = dist[h][w] + 1

ans = 0
for i in range(H):
    ans = max(ans, max(dist[i]))

print(ans)