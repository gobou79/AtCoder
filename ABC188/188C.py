N = int(input())
a = list(map(int, input().split()))

a_1 = a[:2**(N-1)]
a_2 = a[2**(N-1):]

max_a_1 = max(a_1)
max_a_2 = max(a_2)

if max_a_1<max_a_2:
    print(a.index(max_a_1)+1)
else:
    print(a.index(max_a_2)+1)
