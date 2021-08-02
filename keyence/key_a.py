N = int(input())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

a_max = a[0]

c = a[0] * b[0]

print(c)

for i in range(1,N):
    a_max = max(a_max, a[i])
    d = a_max * b[i]
    c = max(c, d)
    print(c)    