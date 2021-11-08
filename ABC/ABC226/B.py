N = int(input())
S = set()

for i in range(N):
    a = tuple(input().split())
    S.add(a)

print(len(S))