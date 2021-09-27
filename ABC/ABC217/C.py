N = int(input())
p = list(map(int, input().split()))

q = {}
for i in range(N):
    q[p[i]] = i+1

ans = []

for i in range(1, N+1):
    ans.append(q[i])

print(*ans)