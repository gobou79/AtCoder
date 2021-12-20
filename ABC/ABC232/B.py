S = list(input())
T = input()

abc = "abcdefghijklmnopqrstuvwxyz"
A = abc * 2

for i in range(26):
    U = []
    for j in range(len(S)):
        U.append(abc[(abc.index(S[j])+i)%26])
    u = "".join(U)
    if u == T:
        print("Yes")
        exit()

print("No")