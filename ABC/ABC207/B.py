import math
A, B, C, D = map(int, input().split())

if C*D <= B:
    print(-1)
else:
    print(math.ceil(A / (C*D - B)))