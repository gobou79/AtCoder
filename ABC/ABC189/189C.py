N = int(input())
A = list(map(int, input().split()))

ans = A[0]

for i in range(N):
    x = A[i]
    for j in range(i, N):
        x = min(x, A[j])
        y = x * (j-i+1)
        ans = max(y, ans)

print(ans)
