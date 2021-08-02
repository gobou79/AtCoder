X = input()
M = int(input())

def henkan(list,shinsu):
    l=len(list)
    ans=0
    for i in range(1,l+1):
        ans+=list[-i]*(shinsu**(i-1))
    return ans

x = list(X)
y = [int(i) for i in list(x)]
n = max(y) + 1
k = 0

while k >= 0:
    N = henkan(y, n)
    if N <= M:
        k += 1
        n += 1
    else:
        break

print(k)