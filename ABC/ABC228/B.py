from collections import deque

N, X = map(int, input().split())
A = list(map(int, input().split()))

ans = 1
a = [False for i in range(N)]
a[X-1] = True

d = deque()
d.append(X-1)

while d:
    v = d.popleft()
    if a[A[v]-1] == True:
        continue
    else:
        ans += 1
        a[A[v]-1] = True
        d.append(A[v]-1)

print(ans)