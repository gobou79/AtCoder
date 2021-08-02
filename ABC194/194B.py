N = int(input())
AB = [map(int, input().split()) for _ in range(N)]
A, B = [list(i) for i in zip(*AB)]

a = sorted(A)
b = sorted(B)

if A.index(min(A)) == B.index(min(B)):
    c = max(a[0], b[1])
    d = max(a[1] , b[1])
    e = min(A)+min(B)
    print(min(c, d, e))
else:
    print(max(min(A), min(B)))
