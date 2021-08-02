nx = list(map(int,input().split()))

vp = [list(map(int, input().split())) for _ in range(nx[0])]
n = nx[0]
x = nx[1] * 100

b = []


for i in range(n):
    b.append(vp[i][0] * vp[i][1])

k = 0

for i in range(n):
    k += b[i]
    if k > x:
        print(i+1)
        break

if k <= x:
    print(-1)