import itertools

N, K = map(int, input().split())
T = []

for i in range(N):
    t = list(map(int, input().split()))
    T.append(t)

comb = list(itertools.permutations(range(2, N+1)))

ans = 0

for i in range(len(comb)):
    c = T[0][comb[i][0]-1] + T[comb[i][-1]-1][0]
    for j in range(len(comb[i])-1):
        c += T[comb[i][j]-1][comb[i][j+1]-1]
    if c == K:
        ans += 1

print(ans)
