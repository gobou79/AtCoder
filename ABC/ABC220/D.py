N = int(input())
A = list(map(int, input().split()))
mod = 998244353

dp_1 = [0 for i in range(10)]

for i in range(N):
    dp_2 = [0 for k in range(10)]
    if i == 0:
        dp_1[A[i]] += 1
    else:
        for j in range(10):
            x = (j + A[i]) % 10
            y = (j * A[i]) % 10
            dp_2[x] += dp_1[j]
            dp_2[y] += dp_1[j] 
        dp_1 = dp_2

for i in range(10):
    print(dp_1[i] % mod)