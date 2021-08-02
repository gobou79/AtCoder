S = list(input())

k = 0
ans = 0

while k < 12:
    if S[k] == "Z" and S[k+1] == "O" and S[k+2] == "N" and S[k+3] == "e":
        ans += 1
        k += 4
    else:
        k += 1

print(ans)

