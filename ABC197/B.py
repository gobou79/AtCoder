H, W, X, Y = map(int, input().split())

S = []
for _ in range(H):
    a = input()
    b = list(str(a))
    S.append(b)

k = 1

x_0 = X-2
x_1 = X
y_0 = Y-2
y_1 = Y

while x_0 >= 0:
    if S[x_0][Y-1] == '.':
        k += 1
        x_0 -= 1
    else:
        break

while y_0 >= 0:
    if S[X-1][y_0] == '.':
        k += 1
        y_0 -=1
    else:
        break

while x_1 < H:
    if S[x_1][Y-1] == '.':
        k += 1
        x_1 += 1
    else:
        break


while y_1 < W:
    if S[X-1][y_1] == '.':
        k += 1
        y_1 += 1
    else:
        break

print(k)
