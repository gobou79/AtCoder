import heapq
from collections import deque

Q = int(input())
B = deque()
A = []
k = 0

for i in range(Q):
    x = list(map(int, input().split()))
    if x[0] == 1:
        B.append(x[1])
    elif x[0] == 2:
        if len(A) != 0:
            print(heapq.heappop(A))
        else:
            print(B.popleft())
    else:
        if k == 0:
            A = list(B)
            heapq.heapify(A)
            k = 1
            B = deque()
        else:
            B = list(B)
            for i in B:
                heapq.heappush(A, i)
            B = deque()