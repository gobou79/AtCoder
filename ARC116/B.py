N = int(input())

A = list(map(int, input().split()))
A.sort()

ans = A[0] ** 2
m = A[0]

for i in A[1:]:
    ans += i * (i + m)
    m = 2 * m
    m += i

print(ans % 998244353)