from collections import defaultdict

N = int(input())
d = defaultdict(int)

for i in range(N):
    s = input()
    d[s] += 1

ans = sorted(d.items(), key=lambda x:x[1], reverse=True)

print(ans[0][0])