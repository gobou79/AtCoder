n = int(input())
a = list(map(int, input().split()))
k = 0

for i in range(n-1):
    for j in range(n):
        if i<j:
            k += abs(a[i] - a[j])

print(k)