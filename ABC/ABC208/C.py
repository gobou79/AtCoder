N, K = map(int, input().split())
a = list(map(int, input().split()))
A = {}

for i in range(N):
    A[i] = a[i]

A_sort = sorted(A.items(), key=lambda x:x[1])


b = K // N
c = K % N

ans = [b for i in range(N)]
for i in range(c):
    k = A_sort[i][0]
    ans[k] += 1

for i in range(N):
    print(ans[i])