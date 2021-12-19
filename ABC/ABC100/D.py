import itertools

N, M = map(int, input().split())

A = []
for i in range(N):
    a = list(map(int, input().split()))
    A.append(a)

L = list(itertools.product([-1, 1], repeat=3))

ans = []

for l in L:
    B = []
    for i in range(N):
        B.append(A[i][0]*l[0] + A[i][1]*l[1] + A[i][2]*l[2])
    B.sort(reverse=True)
    ans.append(sum(B[:M]))

print(max(ans))