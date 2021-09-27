A = input()
B = input()
C = input()
x = input()

ans = ""

for i in range(len(x)):
    if x[i] == "1":
        ans = ans + A
    elif x[i] == "2":
        ans = ans + B
    else:
        ans = ans + C

print(ans)