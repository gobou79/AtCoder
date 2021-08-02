N, Q = map(int, input().split())
A = list(map(int, input().split()))
K = []
for i in range(Q):
    K.append(int(input()))

def saiki(i, k):
    if i == -1:
        return k
    elif A[i] - (i + 1) < k:
        ans = k + i + 1
        return ans
    else:
        saiki(i-1, k)


for i in range(Q):
    if K[i] > len(A):
        print(saiki(len(A)-1, K[i]))
    else:
        print(saiki(K[i]-1, K[i]))
