from collections import deque, defaultdict

M = int(input())
g = [[] for i in range(9)]

for i in range(M):
    u, v = map(int, input().split())
    g[u-1].append(v-1)
    g[v-1].append(u-1)

p = list(map(int, input().split()))

S = ['8' for i in range(9)]

for i in range(8):
    S[p[i]-1] = '{}'.format(i)

s = ''.join(S)

q = deque()
d = defaultdict(int)

q.append(s)
d[s] = 1

while q:
    s = q.popleft()
    for i in range(9):
        if s[i] == '8':
            v = i
    
    for u in g[v]:
        t = list(s)
        t[u], t[v] = t[v], t[u]
        T = ''.join(t)
        if d[T] != 0:
            continue
        else:
            d[T] = d[s] + 1
            q.append(T)

if d['012345678'] == 0:
    print(-1)
else:
    print(d['012345678']-1)