N = int(input())

A, B = [], []
c = 0

for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    c += a/b

d = c/2
ans = 0
t = 0

for i in range(N):
    t_a = t + A[i]/B[i]
    if t_a > d:
        ans += B[i] * (d-t)
        break
    else:
        ans += A[i]
        t = t_a

print(ans)