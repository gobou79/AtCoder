N, P = map(int, input().split())

mod = 1000000007

a = P-1
b = P-2

ans = a * pow(b, N-1, mod) % mod

print(ans)