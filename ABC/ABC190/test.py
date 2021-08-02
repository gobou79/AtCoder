n = 24

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

c = divisor(n)
d = []
for i in c:
    d.append(-i)

d = d + c

print(d)