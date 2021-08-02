n = int(input())
xy = [map(int, input().split()) for _ in range(n)]
x, y = [list(i) for i in zip(*xy)]
k = 0

for i in range(n):
    for j in range(n):
        if i != j and i>j:
            a = (y[i] - y[j])/(x[i]-x[j])
            if -1<=a<=1:
                k += 1
print(k)
