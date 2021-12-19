N = int(input())
A = list(map(int, input().split()))

ans = 0

for i in range(1, 50):
    mod = 2 ** i
    for j in range(N):
        if A[j] % mod == 0:
            ans += 1

print(ans)