T = int(input())

case = []
for _ in range(T):
    case.append(int(input()))

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

for i in case:
    l = divisor(i)
    odd = 0
    even = 0
    for j in l:
        if j % 2 == 1:
            odd += 1
        else:
            even += 1
    if odd > even:
        print("Odd")
    elif even > odd:
        print("Even")
    else:
        print("Same")