import itertools

N = list(input())

choice = list(itertools.permutations(N))
ans = 0

for i in range(len(choice)):
    for j in range(1, len(N)):
        a = choice[i][:j]
        b = choice[i][j:]
        if a[0] == 0 or b[0] == 0:
            break
        A = int(''.join(a))
        B = int(''.join(b))
        if A*B > ans:
            ans = A*B

print(ans)