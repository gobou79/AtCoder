import math

N = int(input())
A = 1
while A ** 3 <= N:
    A+=1

ans = 0

for a in range(1, A):
    n = N // a
    b = a
    while b ** 2 <= n:
        ans += n//b - b + 1
        b += 1

print(ans)