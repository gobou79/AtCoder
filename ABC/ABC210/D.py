H, W, C = map(int, input().split())

A = []

for i in range(H):
    A.append(list(map(int, input().split())))

ans = 1000000000

for i in range(H):
    for j in range(W):
        if i < j:
            
