def f(x_1, x_2, y_1, y_2, x, y):
    sahen = (x_2-x_1)*(y-y_1)
    uhen = (y_2 - y_1)*(x - x_1)
    if sahen == uhen:
        return(True)
    else:
        return(False)

N = int(input())

x, y = [], []

for i in range(N):
    X, Y = map(int, input().split())
    x.append(X)
    y.append(Y)

ans = "No"

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if f(x[i], x[j], y[i], y[j], x[k], y[k]):
                ans = "Yes"
                break

print(ans)