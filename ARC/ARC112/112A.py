T = int(input())

case = [list(map(int, input().split())) for l in range(T)]

for i in range(T):
    if case[i][1] >= 2 * case[i][0]:
        k = ((case[i][1] - 2 * case[i][0] + 2) * (case[i][1] - 2 * case[i][0] + 1)) // 2
        print(k)
    else:
        print(0)