n, s, d = map(int, input().split())

ab = [map(int, input().split()) for _ in range(n)]
a, b = [list(i) for i in zip(*ab)]

k = 0

for i in range(n):
    if a[i] < s and b[i] > d:
        print("Yes")
        k += 1
        break

if k == 0:
    print("No")        
