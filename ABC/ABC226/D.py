N = int(input())
X, Y = [], []
for i in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

s = set()
b = False

for i in range(N-1):
    for j in range(i+1, N):
        if X[i] - X[j] == 0:
            b = True
        else:
            a = (Y[i] - Y[j]) / (X[i] - X[j])
            s.add(a)

if b:
    print(len(s) * 2 + 2)
else:
    print(len(s) * 2)