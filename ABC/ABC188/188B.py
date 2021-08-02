N = int(input())

A = list(map(int,input().split()))
B = list(map(int,input().split()))
k = 0

for i in range(N):
    k += A[i] * B[i]

if k == 0:
    print('Yes')
else:
    print('No')