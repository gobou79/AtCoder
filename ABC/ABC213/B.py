N = int(input())
A = list(map(int, input().split()))

m = max(A)
ans = 0
index = -1

for i in range(N):
    if A[i] > ans and A[i] < m:
        ans = A[i]
        index = i+1


print(index)