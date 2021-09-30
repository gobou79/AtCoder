from collections import Counter

S = input()

if len(S) == 1:
    if int(S) % 8 == 0:
        print("Yes")
    else:
        print("No")
    exit()
elif len(S) == 2:
    if int(S) % 8 == 0 or int(S[1]+S[0]) % 8 == 0:
        print("Yes")
    else:
        print("No")
    exit()

cnt = Counter(S)

for i in range(104, 1000, 8):
    cnt_a = Counter(str(i))
    ans = 0
    for i in cnt_a:
        if cnt[i] < cnt_a[i]:
            break
        else:
            ans += 1
    if ans == len(cnt_a):
        print("Yes")
        exit()

print("No")
