N, K = map(int, input().split())

a = K * (K+1) // 2
ans = a * N + 100 * K * N * (N+1) //2
print(ans)