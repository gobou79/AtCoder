n = int(input())
ab = [map(int, input().split()) for _ in range(n)]
a, b = [list(i) for i in zip(*ab)]
c = []
for i in range(n):
    c.append(a[i] + b[i])
t_a = sum(a)
t_b = 0
k = 0
while t_b <= t_a:
    t_b += max(c)
    i = c.index(max(c))
    c.remove(max(c))
    t_a -= a[i]
    k += 1

print(k)

