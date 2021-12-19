N = int(input())
red = []
for i in range(N):
    x, y = map(int, input().split())
    red.append([x, y])
blue = []
for i in range(N):
    x, y = map(int, input().split())
    blue.append([x, y])

red_sort = sorted(red)
blue_sort = sorted(blue)
ans = 0

for i in range(N):
    x_blue = blue_sort[i][0]
    y_blue = blue_sort[i][1]
    diff = []
    for j in range(len(red_sort)):
        x_red = red_sort[j][0]
        y_red = red_sort[j][1]
        if x_blue > x_red and y_blue > y_red:
            diff.append([x_red, y_red])
    if len(diff) == 0:
        continue
    de_x = -1
    de_y = -1
    ma = 0
    for k, l in diff:
        if l >= ma:
            de_x = k
            de_y = l
            ma = l
    red_sort.remove([de_x, de_y])
    ans += 1

print(ans)