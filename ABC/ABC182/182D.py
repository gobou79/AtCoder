N = int(input())
A = list(map(int, input().split()))

r = []
Ma = []
w = 0
m = -float('inf')

for i in range(N):
    w += A[i]
    r.append(w)

    if i == 0:
        Ma.append(w)
        m = w
    else:
        if w > m:
            Ma.append(w)
            m = w
        else:
            Ma.append(m)

ans = 0
z = 0

for i in range(N):
    ans = max(ans, z+Ma[i])
    z += r[i]

print(ans)