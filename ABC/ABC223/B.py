from collections import deque

S = input()
ans = [S]

for i in range(len(S)-1):
    s = deque(list(S))
    a = s.popleft()
    s.append(a)
    S = ''.join(s)
    ans.append(S)

ans = sorted(ans)

print(ans[0])
print(ans[-1])