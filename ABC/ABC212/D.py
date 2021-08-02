import bisect
from collections import deque

Q = int(input())

l = deque([])
cnt = 0

for i in range(Q):
    a = list(map(int, input().split()))
    if a[0] == 1:
        b = a[1] - cnt
        index = bisect.bisect_left(l, b)
        l.insert(index, b)
    elif a[0] == 2:
        cnt += a[1]
    else:
        ans = l.popleft()
        ans += cnt
        print(ans)