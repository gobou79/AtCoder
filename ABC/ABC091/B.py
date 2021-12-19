from collections import defaultdict

d = defaultdict(int)

N = int(input())
for i in range(N):
    s = input()
    d[s] += 1

M = int(input())
for i in range(M):
    t = input()
    d[t] -= 1

d_sort = sorted(d.items(), key=lambda x:x[1], reverse=True)

ans = d_sort[0][1]

if ans < 0:
    print(0)
else:
    print(ans)