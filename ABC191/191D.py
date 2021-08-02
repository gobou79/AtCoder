import math

X, Y, R = map(float, input().split())

a = math.ceil(X - R)
b = math.floor(X + R)
k = 0

for x in range(a, b+1):
    z = math.sqrt((R + x - X) * (R - x + X))
    y_up = math.floor(Y + z)
    y_down = math.ceil(Y - z)
    k += y_up - y_down + 1

print(k)