N, M = map(int, input().split())
A = []
w = {}

for i in range(2*N):
    a = list(input())
    w[i] = 0
    A.append(a)

def janken(m, i, j):
    if A[i][m] == A[j][m]:
        return -1
    elif (A[i][m] == 'G' and A[j][m] == 'C') or (A[i][m] == 'C' and A[j][m] == 'P') or (A[i][m] == 'P' and A[j][m] == 'G'):
        return i
    else:
        return j

for i in range(M):
    for j in range(0, 2*N, 2):
        if i == 0:
            r = janken(i, j, j+1)
            if r != -1:
                w[r] += 1
        else:
            d = sorted(w.items(), key=lambda x:x[1], reverse=True)
            r = janken(i, d[j][0], d[j+1][0])
            if r != -1:
                w[r] += 1

ans = sorted(w.items(), key=lambda x:x[1], reverse=True)

for i in range(2 * N):
    print(ans[i][0]+1)