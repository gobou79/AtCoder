A, B, C = map(int, input().split())

ans = False
for i in range(A, B+1):
    if i % C == 0:
        print(i)
        ans = True
        break

if ans == False:
    print(-1)