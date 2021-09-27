X = input()
alph = {}
for i in range(len(X)):
    alph[X[i]] = i

N = int(input())
S = []
l = 0
for i in range(N):
    s = input()
    if len(s) > l:
        l = len(s)
    S.append(s)

ans = []

for i in range(N):
    li = list(S[i])
    A = []
    for i in range(len(li)):
        A.append(alph[li[i]])
    ans.append(A)

ans.sort()

for i in range(len(ans)):
    b = ""
    c = ans[i]
    for i in c:
        b = b + X[i]
    print(b)
