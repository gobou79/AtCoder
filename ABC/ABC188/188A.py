a = list(map(int,input().split()))

b = abs(a[0]-a[1])

if b < 3:
    print('Yes')
else:
    print('No')