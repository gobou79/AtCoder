from collections import defaultdict
from math import factorial

cnt = defaultdict(int)

N = int(input())
X = []
Y = []

for i in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

for i in range(N):
    for j in range(i+1, N):
        if Y[i] == Y[j]:
            if X[i] < X[j]:
                cnt["{}_{}".format(X[i], X[j])] += 1
            else:
                cnt["{}_{}".format(X[j], X[i])] += 1

ans = 0

for i in cnt.values():
    if i != 1:
        ans += factorial(i) // (factorial(i-2) * 2)

print(ans)