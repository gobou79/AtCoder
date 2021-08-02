N = int(input())
A = list(map(int, input().split()))

l = len(A)
a = set(A)

if l == len(a):
    print("Yes")
else:
    print("No")