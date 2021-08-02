N, X = map(int, input().split())
S = input()
s = list(S)

for i in range(len(s)):
    if s[i] == 'o':
        X += 1
    elif X != 0:
        X -= 1

print(X)