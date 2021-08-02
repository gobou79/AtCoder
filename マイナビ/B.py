N = int(input())
list = []
for i in range(N):
    a,b=input().split()
    list.append([a, int(b)])

ans = sorted(list, reverse=True, key=lambda x: x[1])

print(ans[1][0])