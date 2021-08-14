H, W, N = map(int, input().split())

A = []
B = []

for i in range(N):
    a, b = map(int, input().split())
    A.append(a-1)
    B.append(b-1)

C = sorted(set(A))
D = sorted(set(B))

E = {v: i+1 for i, v in enumerate(C)}  #数値vがi*1番目と保存しておく辞書
F = {v: i+1 for i, v in enumerate(D)}  #数値vがi*1番目と保存しておく辞書

for i in range(N):
    print(E[A[i]], F[B[i]])
