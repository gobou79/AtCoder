from collections import deque

N, Q = map(int, input().split())

front = [-1 for i in range(N)]
back = [-1 for i in range(N)]

for i in range(Q):
    A = list(map(int, input().split()))
    if A[0] == 1:
        front[A[2]-1] = A[1] - 1
        back[A[1]-1] = A[2] - 1
    elif A[0] == 2:
        front[A[2]-1] = -1
        back[A[1]-1] = -1
    else:
        ans = deque()
        x = A[1]
        ans.append(x)
        while front[x-1] > -1:
            x = front[x-1]+1
            ans.appendleft(x)
        x = A[1]
        while back[x-1] > -1:
            x = back[x-1]+1
            ans.append(x)
        print(len(ans), *ans)