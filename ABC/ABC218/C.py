import numpy as np

N = int(input())

S = []
T = []

def kannsuu(A):
    X = []
    Y = []
    cnt = 0
    for i in range(N):
        for j in range(N):
            if A[i][j] == 1 and cnt == 0:
                y, x = i, j
                cnt = 1
            elif A[i][j] == 1:
                X.append(x-j)
                Y.append(y-i)
    return X, Y


for i in range(N):
    s = list(input())
    a = []
    for i in range(N):
        if s[i] == "#":
            a.append(1)
        else:
            a.append(0)
    S.append(a)

S = np.array(S)

for i in range(N):
    t = list(input())
    a = []
    for i in range(N):
        if t[i] == "#":
            a.append(1)
        else:
            a.append(0)
    T.append(a)

T_0 = np.array(T)
T_1 = np.rot90(T)
T_2 = np.rot90(T_1)
T_3 = np.rot90(T_2)

ans = "No"

X, Y = kannsuu(S)
X_0, Y_0 = kannsuu(T_0)
X_1, Y_1 = kannsuu(T_1)
X_2, Y_2 = kannsuu(T_2)
X_3, Y_3 = kannsuu(T_3)

if X == X_0 and Y == Y_0:
    ans = "Yes"
elif X == X_1 and Y == Y_1:
    ans = "Yes"
elif X == X_2 and Y == Y_2:
    ans = "Yes"
elif X == X_3 and Y == Y_3:
    ans = "Yes"

print(ans)