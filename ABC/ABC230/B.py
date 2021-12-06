S = input()

if len(S) < 3:
    if S == "oo":
        print("No")
        exit()
    else:
        print("Yes")
        exit()
elif len(S) == 3:
    if S == "xxx":
        print("No")
        exit()
b = False

for i in range(3):
    if S[i] == "o":
        a = i
        b = True
        break

if b == False:
    print("No")
    exit()

ans = True

for i in range(len(S)):
    if i%3 == a:
        if S[i] == "x":
            ans = False
            break
        else:
            continue
    else:
        if S[i] == "o":
            ans = False
            break
        else:
            continue

if ans:
    print("Yes")
else:
    print("No")