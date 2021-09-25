import itertools

N, M = map(int, input().split())
A, B = [], []
for i in range(M):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

K = int(input())
C, D = [], []
for i in range(K):
    c, d = map(int, input().split())
    C.append(c)
    D.append(d)

choice = list(itertools.product([0, 1], repeat=K))
ans = 0

for i in range(len(choice)):
    s = set([])
    cnt = 0
    for j in range(K):
        if choice[i][j] == 0:
            s.add(C[j])
        else:
            s.add(D[j])
    for i in range(M):
        if A[i] in s and B[i] in s:
            cnt += 1
    if cnt > ans:
        ans = cnt

print(ans)
