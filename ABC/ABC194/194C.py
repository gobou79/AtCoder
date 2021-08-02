N = int(input())
A = list(map(int, input().split()))
A_1 = []
A_2 = []
a = A[0]

for i in range(len(A)):
    A_2.append((N-1) * (A[i]**2))

for i in range(len(A)-1):
    A_1.append(2 * (A[i+1]*a))
    a += A[i+1]

ans = sum(A_2) - sum(A_1)

print(ans)
