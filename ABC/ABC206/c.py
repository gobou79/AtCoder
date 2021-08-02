import collections

N = int(input())
A = list(map(int, input().split()))

B = collections.Counter(A)
ans = 0

cnt = sum(B.values())

for i in B.values():
    cnt -= i
    ans += cnt * i

print(ans)