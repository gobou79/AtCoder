from collections import deque

S = list(input())
T = deque([])
cnt = 0

for i in range(len(S)):
    if S[i] == "R":
        cnt += 1
    else:
        if cnt % 2 == 0:
            if len(T) != 0 and T[-1] == S[i]:
                T.pop()
            else:
                T.append(S[i])
        else:
            if len(T) != 0 and T[0] == S[i]:
                T.popleft()
            else:
                T.appendleft(S[i])

T = list(T)
if cnt % 2 == 1:
    T.reverse()

print("".join(T))