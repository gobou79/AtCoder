def binary_search(data, value):
    left = 0 
    right = len(data) - 1 
    while left <= right:
        mid = (left + right) // 2
        if value == data[mid]:
            return mid
        elif value > data[mid]:
            left = mid + 1  
        else:
            right = mid - 1
    return left

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

ans = 10000000000

for i in range(M):
    left = binary_search(A, B[i])
    if left == len(A):
        can = B[i] - A[left - 1]
        if ans > can:
            ans = can
    elif left == 0:
        can = abs(A[left] - B[i])
        if ans > can:
            ans = can
    else:
        can = min(abs(A[left]-B[i]), abs(B[i] - A[left-1]))
        if ans > can:
            ans = can

print(ans)


