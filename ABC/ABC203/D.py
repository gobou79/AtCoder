import math
import statistics
import numpy as np

N, K = map(int, input().split())

a = [list(map(int, input().split())) for l in range(N)]
a = np.array(a)

#m = math.floor(K ** 2 /2) + 1
b = N - K + 1

ans = 10 ** 9


for h in range(b):
    for w in range(b):
        l = a[h:h+K, w:w+K]
        d = l.flatten()
        c = statistics.median_low(d)
        if ans > c:
            ans = c

print(ans)



