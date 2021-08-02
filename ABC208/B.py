P = int(input())

coin = [1]

for i in range(2, 11):
    coin.append(coin[i-2] * i)

ans = 0
cnt = [0 for i in range(10)]

def f(P):
    for i in reversed(range(0, 10)):
        if P >= coin[i] and cnt[i]<=100:
            P -= coin[i]
            break
    return(P)

while P>0:
    P = f(P)
    ans += 1

print(ans)

