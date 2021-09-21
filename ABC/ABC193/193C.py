import math

N = int(input())

a_max = math.floor(math.sqrt(N))
b_max = math.floor(math.log2(N))

cnt = []

for a in range(2, a_max+1):
    for b in range(2, b_max+1):
        if math.pow(a, b) <= N:
            cnt.append(math.pow(a, b))
        else:
            break

cnt = set(cnt)

print(N - len(cnt))
