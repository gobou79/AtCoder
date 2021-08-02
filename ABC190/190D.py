N = int(input())
N = 2 * N

def divisor(n): 
    i = 1
    table = []
    while i * i <= n:
        if n%i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = list(set(table))
    return table

c = divisor(N)
d = []
for i in c:
    d.append(-i)

x = d + c
y = [N // i for i in x]
k = 0

for i in range(len(x)):
    if (x[i] + y[i]+1) % 2 == 0:
        k += 1

print(k//2)