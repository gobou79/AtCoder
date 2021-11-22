N, K = map(int, input().split())
score = []
d = {}
for i in range(N):
    a, b, c = map(int, input().split())
    score.append(a+b+c)

B = sorted(score, reverse=True)

sk = B[K-1]

for i in range(N):
    if score[i] + 300 >= sk:
        print("Yes")
    else:
        print("No")