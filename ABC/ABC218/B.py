P = list(map(int, input().split()))

S = "abcdefghijklmnopqrstuvwxyz"

ans = ""

for i in range(26):
    ans = ans + S[P[i]-1]

print(ans)