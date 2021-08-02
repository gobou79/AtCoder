import math
X = list(input())

for i in range(len(X)):
    if X[i] == ".":
        del X[i:]
        break
x = ''.join(X)

print(x)