import copy

N, M, Q = map(int, input().split())
WV = [list(map(int, input().split())) for _ in range(N)]
# W, V = [list(i) for i in zip(*WV)]
X = list(map(int, input().split()))
AB = list(map(int, input().split()) for _ in range(Q))
A, B = [list(i) for i in zip(*AB)]

WV = sorted(WV, reverse=True, key=lambda x: x[1])

for i in range(Q):
    x = copy.copy(X)
    del x[A[i]-1:B[i]]
    x.sort()
    v = 0
    wv = copy.copy(WV)
    for j in range(len(x)):
        for k in range(N):
            if x[j] >= wv[k][0]:
                v += wv[k][1]
                wv[k][0] = 10 ** 7
                break
    print(v)

