from collections import defaultdict

N, K = map(int, input().split())
c = list(map(int, input().split()))

d = defaultdict(int)

for i in range(K):
    d[c[i]] += 1

ans = len(set(c[:K]))
k = ans

for i in range(K, N):
    d[c[i-K]] -= 1
    if d[c[i-K]] == 0:
        k -= 1
    if d[c[i]] == 0:
        k += 1
    d[c[i]] += 1
    if ans < k:
        ans = k

print(ans)