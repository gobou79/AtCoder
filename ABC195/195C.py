N = int(input())

n = str(N)
k = len(n)
c = 0
r = [4, 7, 10, 13, 16, 19]

for i in range(10):
    if k > r[i] and k >= r[i+1]:
        c += (10 ** (r[i+1]-1) - 10 ** (r[i]-1)) * (i+1)
    elif k >= r[i] and k < r[i+1]:
        c += (N - 10 ** (r[i]-1) +1) * (i+1)
    else:
        break

print(c)
