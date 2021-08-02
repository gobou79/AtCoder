
import itertools

N, M= map(int, input().split())

cond = [list(map(int, input().split())) for _ in range(M)]

K = int(input())

choice = [tuple(map(int, input().split())) for _ in range(K)]

ans = 0

for balls in itertools.product(*choice):
    balls = set(balls)
    cnt = sum(A in balls and B in balls for A, B in cond)
    if ans < cnt:
        ans = cnt

print(ans)