N, M, T = map(int, input().split())

A = []
B = []

n = N

for i in range(M):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

t = 0
ans = 0

for i in range(M):
    n -= A[i] - t
    if n <= 0:
        ans = 1
        print("No")
        break
    else:
        n += (B[i] - A[i])
        if n > N:
            n = N
        t = B[i]

if ans == 0 and n - (T - t) > 0:
    print("Yes")
elif ans == 0:
    print("No")