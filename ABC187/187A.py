def digit_sum(n):
    s = str(n)
    array = list(map(int, s))
    return(sum(array))


a = list(map(int,input().split()))
b = a[0]
c = a[1]
print(max(digit_sum(b), digit_sum(c)))