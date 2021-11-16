N = int(input())
S = list(map(int, input().split()))

def f(a, b):
    return (4*a+3)*(4*b+3)

ans = [False for i in range(N)]

for i in range(N):
    for j in range(1, 201):
        for k in range(1, 201):
            if f(j, k) == 4 * S[i] + 9:
                ans[i] = True
cnt = 0

for i in range(N):
    if ans[i]:
        continue
    else:
        cnt+=1  

print(cnt)