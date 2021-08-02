S = input()
l = list(S)

for i in range(len(l)):
    if l[i] == "6":
        l[i] = "9"
    elif l[i] == "9":
        l[i] = "6"
l.reverse()

print(''.join(l))