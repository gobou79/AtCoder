N, K = map(int, input().split())
list = []
for i in range(N):
    a,b=input().split()
    list.append([int(a), int(b)])

list = sorted(list, reverse=False, key=lambda x: x[0]) 

ans = K

for i in range(N):
    if list[i][0] <= ans:
        ans += list[i][1]

print(ans)