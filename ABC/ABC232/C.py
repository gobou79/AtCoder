import itertools
import copy

N, M = map(int, input().split())
gt = [[] for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    gt[a-1].append(b-1)
    gt[b-1].append(a-1)
ga = [[] for i in range(N)]
for j in range(M):
    c, d = map(int, input().split())
    ga[c-1].append(d-1)
    ga[d-1].append(c-1)

L = list(itertools.permutations([i for i in range(N)]))

for i in range(N):
    gt[i].sort()

for A in L:
    cnt = 0
    for j in range(N):
        B = []
        for k in ga[A[j]]:
            B.append(A.index(k))
        B.sort()
        if gt[j] == B:
            cnt += 1
        else:
            break
    if cnt == N:
        print("Yes")
        exit()

print("No")