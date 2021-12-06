import math
N = int(input())

k_0 = int(math.sqrt(N))
ans = 0

for k in range(1, k_0+1):
    ans += (N//k - N//(k+1)) * k

for i in range(1, N//(k_0+1)+1):
    ans += N//i

print(ans)