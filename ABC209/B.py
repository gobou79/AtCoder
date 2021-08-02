N, X = map(int, input().split())

A = list(map(int, input().split()))

ans = 0

for i in range(N):
    if (i+1) % 2 == 0:
        ans += A[i] - 1
    else:
        ans += A[i]

if ans <= X:
    print("Yes")
else:
    print("No")