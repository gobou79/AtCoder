K = int(input())
S = list(input())
T = list(input())

S.pop(-1)
T.pop(-1)

S = list(map(int, S))
T = list(map(int, T))
k = 1
c = (9 * K - 8) * (9 * K - 9)

def total(l):
    a = 0
    for i in range(1,10):
        a += i * 10 ** l[i-1]
    return(a)

total_s = [i * 0 for i in range(9)]
total_t = [i * 0 for i in range(9)]

for i in S:
    total_s[i-1] += 1
for i in T:
    total_s[i-1] += 1


for i in range(9):
    a = total_s[i] + total_t[i]
    if a < K:
        total_s[i] += 1
        takahashi = total(total_s)
        for j in range(9):
            b = total_s[j] + total_t[j]
            if b < K:
                total_t[j] += 1
                aoki = total(total_t)
                if takahashi > aoki:
                    k += (K - a) * (K - b) / c
print(k)





