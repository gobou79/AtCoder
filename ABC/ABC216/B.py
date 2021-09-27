N = int(input())

S, T = [], []

for i in range(N):
    s, t = input().split()
    S.append(s)
    T.append(t)

ans = 0

for i in range(N):
    for j in range(i+1, N):
        if S[i] == S[j]:
            if T[i] == T[j]:
                ans = 1

if ans == 0:
    print("No")
else:
    print("Yes")