S = input()

s = list(S)

k = 0

for i in range(len(s)):
    if i % 2 == 0:
        if s[i].isupper():
            k = 1
            break
    else:
        if s[i].islower():
            k = 1
            break
if k == 0:
    print('Yes')
else:
    print('No')