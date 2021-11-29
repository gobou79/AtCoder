s1 = input()
s2 = input()

ans = False

for i in range(2):
    if s1[i] == s2[i] == "#":
        ans = True
if s1[0] == s1[1] or s2[0] == s2[1]:
    ans = True

if ans:
    print("Yes")
else:
    print("No")