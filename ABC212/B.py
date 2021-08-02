X = input()

ans = 0
if X[0] == X[1] and X[1] == X[2] and X[2] == X[3]:
    print("Weak")
else:
    for i in range(3):
        if int(X[i]) == int(X[i+1]) - 1:
            ans += 1
        elif int(X[i]) == 9 and int(X[i+1]) == 0:
            ans += 1
        else:
            break
    if ans == 3:
        print("Weak")
    else:
        print("Strong")