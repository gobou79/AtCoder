N = list(input())


while len(N) != 0 and N[-1] == "0":
    N.pop(-1)

M = list(reversed(N))
k = 0
for i in range(len(N)):
    if N[i] == M[i]:
        k += 1
    else:
        break
if k == len(N):
    print("Yes")
else:
    print("No")