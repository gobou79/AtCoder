from collections import deque

N = int(input())

ans = deque()

while N > 0:
    if N % 2 == 0:
        ans.appendleft('B')
        N = N // 2
    else:
        ans.appendleft('A')
        N -= 1

print(*ans, sep='')
