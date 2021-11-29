from collections import  deque

S = input()
K = int(input())

d = deque()
index_left = 0
cnt = 0
ans = 0

for i in range(len(S)):
    if S[i] == ".":
        cnt += 1
        d.append(i)
        if cnt > K:
            j = d.popleft()
            cnt -= 1
            ans = max(ans, i-index_left)
            index_left = j+1

print(max(ans, len(S)-index_left))