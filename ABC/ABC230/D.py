from collections import defaultdict

N, D = map(int, input().split())
section = []

for i in range(N):
    l, r = map(int, input().split())
    section.append([r, l])

section.sort()
ans = 0
right = 0

for i in range(N):
    if i == 0:
        ans += 1
        right = section[i][0]
    else:
        if section[i][1] <= right + D - 1:
            continue
        else:
            ans += 1
            right = section[i][0]

print(ans)