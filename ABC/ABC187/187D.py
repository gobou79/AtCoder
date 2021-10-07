N = int(input())
X = 0
C = []

for i in range(N):
    a, b = map(int, input().split())
    X -= a
    C.append(2 * a + b)

C.sort(reverse=True)

cnt = 0

while X <= 0:
    X += C[cnt]
    cnt += 1

print(cnt)
