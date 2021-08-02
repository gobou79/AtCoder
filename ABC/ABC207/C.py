N = int(input())
t = []
l = []
r = [] 

for i in range(N):
    a, b, c = map(int, input().split())
    if a == 2:
        c -= 0.1
    elif a == 3:
        b += 0.1
    elif a == 4:
        b += 0.1
        c -= 0.1
    t.append(a)
    l.append(b)
    r.append(c)

ans = 0

for i in range(N):
    for j in range(i+1, N):
        if l[i] <= r[j] and l[j] <= r[i]:
            ans += 1
        elif l[j] <= r[i] and l[i] <= r[j]:
            ans += 1
        elif l[i] <= l[j] and r[i] >= r[j]:
            ans += 1
        elif l[j] <= l[i] and r[j] >= r[i]:
            ans += 1

print(ans)