S = list(input())
T = list(input())

for i in range(len(S)-1):
    if S[i] != T[i]:
        T[i], T[i+1] = T[i+1], T[i]
        break

s = ','.join(S)
t = ','.join(T)


if S == T:
    print("Yes")
else:
    print("No")