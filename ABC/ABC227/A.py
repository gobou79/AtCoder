N, K, A = map(int, input().split())

ans = (K % N) + A - 1

if ans % N == 0:
    print(N)
else:
    print(ans%N)