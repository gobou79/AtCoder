import math

N = int(input())
A = list(map(int, input().split()))
X = int(input())

A_sum = sum(A)

x = X//A_sum

total = A_sum * x

if total > X:
    print(len(A) * x)
else:
    for i in range(N):
        total += A[i]
        if total > X:
            cnt = i+1
            break
    print(len(A) * x + cnt)    