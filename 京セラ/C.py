import math

N = int(input())
A = list(map(int, input().split()))

s = set()
a = []

for i in A:
    s.add(i % 200)
    a.append(i % 200)

ans = 0

for i in s:
    n = a.count(i)
    if n != 1:
        ans += math.factorial(n) // (2 * math.factorial(n-2))

print(ans)
