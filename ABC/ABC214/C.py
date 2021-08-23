N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

t = min(T)
index = T.index(t)

A = {index:t}

for i in range(1, N):
    a = A[index] + S[index]
    index += 1
    if index == N:
        index = 0
    if a < T[index]:
        A[index] = a
    else:
        A[index] = T[index]

for i in range(N):
    print(A[i])