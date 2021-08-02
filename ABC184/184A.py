a = [list(map(int, input().split())) for _ in range(2)]

print(a[0][0]*a[1][1]-a[0][1]*a[1][0])