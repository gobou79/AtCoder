N = int(input())

A = [0] * N
P = [0] * N
X = [0] * N

l = []

for i in range(N):
    #上から順番に代入していく
    A[i], P[i], X[i] = map(int, input().split())

for i in range(N):
    if A[i]<X[i]:
        l.append(P[i])
if len(l) > 0:
    print(min(l))
else:
    print(-1)

