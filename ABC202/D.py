import math

A, B, K = map(int, input().split())

a = A
b = B
ans = []
cnt = 0
v = []

for i in range(A + B):
    if a > 0 and cnt + math.factorial(a+b-1)//math.factorial(a-1) // math.factorial(b) >= K:
        ans.append('a')
        a -= 1
        v.append(cnt)
    else:
        ans.append('b')
        if a > 0:
            cnt += math.factorial(a+b-1)//math.factorial(a-1) // math.factorial(b)
        b -= 1
        v.append(cnt)

print(''.join(ans))