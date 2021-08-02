nk = list(map(int,input().split()))
a = list(map(int,input().split()))

a.sort()
a_max = max(a)
count = []
for i in range(a_max+1):
    d = a.count(i)
    if d == 0:
        break
    else:
        count.append(d)
c = [i * 0 for i in range(nk[1])]
k = 0

while k < nk[1]:
    c[k] += len(count)
    for i in range(len(count)):
        count[i] -= 1
    if 0 in count:
        index = count.index(0)
        del count[index:]
    if len(count) == 0:
        break
    k += 1

print(sum(c))
