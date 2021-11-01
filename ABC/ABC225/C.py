N, M = map(int, input().split())
B = []
for i in range(N):
    b = list(map(int, input().split()))
    B.append(b)

for i in range(M-1):
    if ((B[0][i+1]-1)%7 != ((B[0][i]-1)%7) + 1) or (B[0][i+1] != B[0][i] + 1):
        print("No")
        exit()

for i in range(N-1):
    for j in range(M):
        if B[i+1][j] != B[i][j] + 7:
            print("No")
            exit()

print("Yes")
