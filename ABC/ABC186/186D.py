N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)

total = sum(A)
ans = 0

for i in range(N-1):
    total -= A[i]
    ans += (N-i-1)*A[i] - total

print(ans)
