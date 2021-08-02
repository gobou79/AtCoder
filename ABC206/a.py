import math
N = int(input())

if 206 - math.floor(1.08 * N) > 0:
    print('Yay!')
elif 206 - math.floor(1.08 * N) == 0:
    print('so-so')
else:
    print(':(')