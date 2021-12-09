from collections import deque

s = input()
t = input()

dp = [[0 for i in range(len(s)+1)] for j in range(len(t)+1)]

for i in range(1, len(t)+1):
    for j in range(1, len(s)+1):
        if s[j-1] == t[i-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

row = len(t)
column = len(s)
value = dp[-1][-1]
ans = deque()
while value>0:
    if dp[row-1][column] < value and dp[row][column-1] < value:
        ans.appendleft(t[row-1])
        row -= 1 
        column -= 1
        value -= 1
    elif dp[row-1][column] < value:
        column -= 1
    elif dp[row][column-1] < value:
        row -= 1
    else:
        row -= 1

print("".join(ans))