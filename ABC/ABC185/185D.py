import math
N, M = map(int, input().split())
if M == 0:
    print(1)
    exit()

A = list(map(int, input().split()))

A.sort()
B = []

for i in range(len(A)-1):
    B.append(A[i+1]-A[i]-1)

B.append(A[0]-1)
B.append(N-A[-1])

s = set(B)
if 0 in s:
    s.remove(0)
C = list(s)

if len(C) == 0:
    print(0)
    exit()

mi = min(C)

ans = 0

for i in range(len(B)):
    ans += math.ceil(B[i]/mi)

print(ans)
