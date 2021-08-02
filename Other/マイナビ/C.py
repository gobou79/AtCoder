import math

S = input()

right = 0
mis = 0
unknown = 0

for i in range(len(S)):
    if S[i] == "o":
        right += 1
    elif S[i] == "x":
        mis += 1
    else:
        unknown += 1

if right > 4:
    print(0)
elif right == 4:
    print(24)
elif right == 3:
    print(36 + 24 * unknown)
elif right == 2:
    print(14 + 12 * unknown ** 2 + 24 * unknown)
elif right == 1:
    print(1 + 4 * unknown ** 3 + 6 * unknown ** 2 + 4 * unknown)
else:
    print(unknown ** 4)