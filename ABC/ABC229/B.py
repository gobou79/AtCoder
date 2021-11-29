A, B = input().split()

l = min(len(A), len(B))
ans = "Easy"

for i in range(l):
    a = int(A[-(i+1)])
    b = int(B[-(i+1)])
    if a + b >= 10:
        ans = "Hard"

print(ans)
