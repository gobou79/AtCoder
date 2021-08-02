import math
A, B = map(int, input().split())

for c in range(B, 0, -1):
    if math.floor(B/c) - math.floor((A-1)/c) > 1:
        print(c)
        break
