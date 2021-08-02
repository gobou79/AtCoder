import collections

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

D = []

cnt = 0

cnt_A = collections.Counter(A)

for i in C:
    D.append(B[i-1])

cnt_D = collections.Counter(D)

for i in range(1, N+1):
    cnt+= cnt_A[i] * cnt_D[i]

print(cnt)