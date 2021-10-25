N = int(input())

X, Y = [], []


for i in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

ans = 0

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if (Y[k]-Y[i])*(X[j]-X[i]) == (Y[j]-Y[i])*(X[k]-X[i]):
                continue
            else:
                ans += 1

print(ans)