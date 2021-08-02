import numpy as np

T = []
N, K = (int(x) for x in input().split())

for i in range(8):
    a = list(map(int,input().split))
    if len(a) != 0:
        T.append(a)
    else:
        break

T_np = np.array(T)


