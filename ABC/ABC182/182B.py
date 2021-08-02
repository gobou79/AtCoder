N = int(input())
A = list(map(int, input().split()))

a_max = max(A)
n_min = 0
num = 0

for i in range(2, a_max+1):
    k = 0
    for j in A:
        if j % i == 0:
            k += 1
    if k >= n_min:
        n_min = k
        num = i

print(num)

