import heapq

Q = int(input())

l = []
cnt = 0

for i in range(Q):
    a = list(map(int, input().split()))
    if a[0] == 1:
        b = a[1] - cnt
        heapq.heappush(l, b)
    elif a[0] == 2:
        cnt += a[1]
    else:
        ans = heapq.heappop(l)
        ans += cnt   
        print(ans)