H, W = map(int, input().split())
A = []
for i in range(H):
    a = list(map(int, input().split()))
    A.append(a)

ans = True

for i in range(H):
    for j in range(i+1, H):
        for k in range(W):
            for l in range(k+1, W):
                if A[i][k] + A[j][l] <= A[j][k] + A[i][l]:
                    continue
                else:
                    ans = False
                    break

if ans:
    print("Yes")
else:
    print("No")